import whisper
import speech_recognition as sr

recognizer = sr.Recognizer()
model = whisper.load_model("base")

def transcribe_from_mic():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)
            with open("temp.wav", "wb") as f:
                f.write(audio.get_wav_data())
            result = model.transcribe("temp.wav")
            return result["text"]
    except Exception as e:
        print(f"Mic error: {e}")
        return ""