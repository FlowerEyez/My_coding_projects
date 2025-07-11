from assistant.speech_input import transcribe_from_mic
from assistant.tts import speak
from assistant.nlp import handle_command

def main():
    speak("Batassistant online. Listening...")
    while True:
        text = transcribe_from_mic()
        if not text:
            continue
        print (f"You said: {text}")
        response = handle_command(text)
        if response:
            speak(response)
        if "shutdown" in text.lower():
            speak("Shutting down. stay safe.")
            break
if __name__ == "__main__":
    main()