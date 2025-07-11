import requests
from datetime import datetime

# Connection settings
REMOTE_OLLAMA_HOST = "http://127.0.0.1:11434"     # Replace with your main machine's IP if needed
LOCAL_OLLAMA_HOST = "http://localhost:11434"

REMOTE_MODEL = "llama3"
LOCAL_MODEL = "tinyllama"
CONNECTION_TIMEOUT = 2

def ask_ollama(prompt: str, host: str, model: str) -> str | None:
    """Send a prompt to an Ollama model using /api/chat and return the response."""
    try:
        response = requests.post(
            f"{host}/api/chat",
            json={
                "model": model,
                "messages": [
                    {"role": "user", "content": prompt}
                ],
                "stream": False
            },
            timeout=CONNECTION_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()
        return data.get("message", {}).get("content", "[No response received]")
    except requests.exceptions.RequestException as e:
        print(f"🔌 Ollama error on {host}: {e}")
        return None

def handle_command(text: str) -> str:
    """Process a voice command or fallback to LLM-based answer."""
    lowered = text.lower()

    # Local keyword-based commands
    if "what time is it" in lowered:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}"

    if "your name" in lowered:
        return "You can call me Batassistant."

    if "shutdown" in lowered:
        return "Shutting down."

    # Attempt remote model first
    print("🔄 Trying remote LLM...")
    remote_response = ask_ollama(text, REMOTE_OLLAMA_HOST, REMOTE_MODEL)
    if remote_response:
        return remote_response.strip()

    # Fallback to local model
    print("⚠️ Remote failed. Using local model...")
    local_response = ask_ollama(text, LOCAL_OLLAMA_HOST, LOCAL_MODEL)
    if local_response:
        return local_response.strip()

    return "Sorry, I couldn't process that right now."
