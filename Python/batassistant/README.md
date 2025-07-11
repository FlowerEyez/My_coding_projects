# BatAssistant - phase 1 (Core Assistant)

A lightweight, modular voice assistant inspired by JARVIS and the Batcomputer

## Features (Phase 1)
- Wake word detection
- Speech-to-text via Whisper
- Command parsing and GPT-4 (possible swap to ollama for local hosting) fallback
- Text-to-speech responses

## Installation

```bash
git clone https://github.com/FlowerEyez/My_coding_projects/tree/main/Python/batassistant.git
cd batassistant
python -m venv venv
source venv/bin/activate # or venv/Scripts/activate on Windows
pip install -r requirements.txt
python main.py