import requests
from datetime import datetime

# Connection settings
REMOTE_OLLAMA_HOST = "http://localhost:11434"  # Use LAN IP if calling from another device
LOCAL_OLLAMA_HOST = "http://localhost:11434"

REMOTE_MODEL = "mistral"
LOCAL_MODEL = "tinyllama"
CONNECTION_TIMEOUT = 10


def ask_ollama(prompt: str, host: str, model: str) -> str | None:
    """
    Send a prompt to an Ollama model using /api/chat (for chat models),
    or fallback to /api/generate (for non-chat models like tinyllama).
    """
    headers = {"Content-Type": "application/json"}

    # Try /api/chat first
    try:
        response = requests.post(
            f"{host}/api/chat",
            headers=headers,
            json={
                "model": model,
                "messages": [{"role": "user", "content": prompt}],
                "stream": False
            },
            timeout=CONNECTION_TIMEOUT
        )
        if response.status_code == 200:
            data = response.json()
            return data.get("message", {}).get("content", "[No response]")
        else:
            print(f"⚠️ Chat API failed ({response.status_code}), trying generate...")
    except requests.exceptions.RequestException as e:
        print(f"🔌 Chat API error on {host}: {e}")

    # Try /api/generate instead (for simple models)
    try:
        response = requests.post(
            f"{host}/api/generate",
            headers=headers,
            json={
                "model": model,
                "prompt": prompt,
                "stream": False
            },
            timeout=CONNECTION_TIMEOUT
        )
        response.raise_for_status()
        data = response.json()
        return data.get("response", "[No response]")
    except requests.exceptions.RequestException as e:
        print(f"🔌 Generate API error on {host}: {e}")
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

    # Try remote model first
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
