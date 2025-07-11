import requests

# Update this to your main computer's IP (LAN)
REMOTE_OLLAMA_HOST = "http://127.0.0.1:11434"
LOCAL_OLLAMA_HOST = "http://localhost:11434"

# Which models you're running
REMOTE_MODEL = "llama3"
LOCAL_MODEL = "tinyllama"

# Timeout for remote check (in seconds)
CONNECTION_TIMEOUT = 2

def ask_ollama(prompt, host, model):
    try:
        response = requests.post(f"{host}/api/generate", json={
            "model": model,
            "prompt": prompt,
            "stream": False
        }, timeout=CONNECTION_TIMEOUT)
        data = response.json()
        return data.get('response', "[No response received]")
    except Exception as e:
        print(f"Ollama error on {host}: {e}")
        return None

def handle_command(text):
    # Local keyword-based commands
    lowered = text.lower()

    if "what time is it" in lowered:
        from datetime import datetime
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    elif "your name" in lowered:
        return "You can call me Batassistant."

    elif "shutdown" in lowered:
        return "Shutting down."

    # Try remote first
    print("🔄 Trying remote LLM...")
    remote_response = ask_ollama(text, REMOTE_OLLAMA_HOST, REMOTE_MODEL)
    if remote_response:
        return remote_response

    # Fallback to local
    print("⚠️ Remote failed. Using local model...")
    local_response = ask_ollama(text, LOCAL_OLLAMA_HOST, LOCAL_MODEL)
    if local_response:
        return local_response

    return "Sorry, I couldn't process that right now."
