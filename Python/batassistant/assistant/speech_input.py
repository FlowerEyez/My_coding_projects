import whisper
import speech_recognition as sr
import os

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
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)

        temp_file = "temp.wav"
        with open(temp_file, "wb") as f:
            f.write(audio.get_wav_data())

        result = model.transcribe(temp_file)

        # Optional: delete temp file after transcription
        os.remove(temp_file)

        return result.get("text", "")
    
    except sr.RequestError:
        print("❌ Could not request results from speech recognition service.")
    except sr.UnknownValueError:
        print("🤷 Speech unintelligible.")
    except Exception as e:
        print(f"⚠️ Mic error: {e}")

    return ""
