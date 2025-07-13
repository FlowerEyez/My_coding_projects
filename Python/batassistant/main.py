import time
from assistant.speech_input import transcribe_from_mic
from assistant.tts import speak
from assistant.nlp import handle_command
from assistant.wake_word import wait_for_wake_word

def main():
    speak("Ruby 0.3 Online, listening...")
    while True:
        wait_for_wake_word() # Blocks input till wake word is detected
        print("👂 Wake word detected. Listening for command...")
        speak("yes?") # cue to tell assistant is ready
        time.sleep(0.2) # adds #sec buffer before recording
        text = transcribe_from_mic()
        if text:
            print(f"🧍 You said: {text}")
            response = handle_command(text)
            print(f"🧠 Assistant: {response}")
            speak(response)
        if "Shut down." in text.lower():
            speak("Shutting down. Stay safe.")
            break

if __name__ == "__main__":
    main()