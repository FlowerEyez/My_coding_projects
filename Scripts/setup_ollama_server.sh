#!/bin/bash

# Get local IP
IP=$(hostname -I | awk '{print $1}')
CONFIG="$HOME/.ollama/config"

echo "Your local IP is: $IP"
echo "Updating Ollama config to listen on 0.0.0.0..."

# Patch config
mkdir -p ~/.ollama
cat <<EOF > "$CONFIG"
[api]
address = "0.0.0.0:11434"
EOF

# Open firewall port (if ufw is enabled)
if command -v ufw &>/dev/null && sudo ufw status | grep -q "Status: active"; then
  echo "UFW detected, allowing port 11434..."
  sudo ufw allow 11434/tcp
else
  echo "No active UFW firewall detected. Skipping firewall config."
fi

echo "✅ Ollama is configured to be accessible from other devices."
echo "▶️ Restart Ollama with:  ollama serve"
echo "🌐 Pi can now send requests to: http://$IP:11434"
