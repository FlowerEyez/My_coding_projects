# BatAssistant - phase 1 (Core Assistant)

A lightweight, modular voice assistant inspired by JARVIS and the Batcomputer

## Features (Phase 1)
- Wake word detection (still buggy, requires tuning but work*) ✔️
- Speech-to-text via Whisper ✔️
- Command parsing and ollama ✔️
- Text-to-speech responses ✔️

## Installation
note: for ollama you will need to set up remote server
https://ollama.com/download
once that is installed pull tinillama for local fallback and Mistral for home server ("ollama pull tinillama/mistral" in terminal). "ollama serve" on port 11434 is default, allowing you to remote access for any internet connection ***
(this is for my own computer once finshed i will rewrite to be alot simpler)

```bash
git clone https://github.com/FlowerEyez/My_coding_projects/tree/main/Python/batassistant.git
cd batassistant
python -m venv venv
source venv/bin/activate # or venv/Scripts/activate on Windows
pip install -r requirements.txt
python main.py