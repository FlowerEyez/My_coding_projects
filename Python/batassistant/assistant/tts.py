import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Optional: Configure voice properties
engine.setProperty('rate', 175)     # Speech speed
engine.setProperty('volume', 1.0)   # Volume (0.0 to 1.0)

def speak(text: str):
    """Convert text to speech and print it for logging."""
    if not text:
        return

    print("Assistant:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except RuntimeError as e:
        print(f"TTS engine error: {e}")
