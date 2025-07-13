import whisper
import speech_recognition as sr
import os
import tempfile
import logging

# prevent Whisper from printing logs to stdout
logging.getLogger("whisper").setLevel(logging.ERROR)

# Load Whisper model
try:
    model = whisper.load_model("base")
except AttributeError:
    raise ImportError("Make sure 'openai-whisper' is installed via 'pip install -U openai-whisper'")

recognizer = sr.Recognizer()

def transcribe_from_mic():
    try:
        with sr.Microphone() as source:
            print("🎙️ Listening for speech...")
            recognizer.adjust_for_ambient_noise(source, duration=1.0) # Helps with background noise
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10) # Prevents cutting off long phrases
        # Write audio as a temp file
        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
            f.write(audio.get_wav_data())
            temp_file = f.name
        # Transcribe with whisper
        result = model.transcribe(temp_file)
        # Optional: delete temp file after transcription
        os.remove(temp_file)

        return result.get("text", "")

    except sr.WaitTimeoutError:
        print("⏱️ No speech detected within timeout.")
    except sr.RequestError:
        print("❌ Could not request results from speech recognition service.")
    except sr.UnknownValueError:
        print("🤷 Speech unintelligible.")
    except Exception as e:
        print(f"⚠️ Mic error: {e}")

    return ""
