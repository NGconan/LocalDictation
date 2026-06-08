# Technical Design

## Architecture

Recorder
↓
Transcriber
↓
Corrector
↓
Clipboard
↓
UI

---

## Recorder

Responsibilities:

- Microphone recording
- WAV generation

Output:

recordings/input.wav

---

## Transcriber

Responsibilities:

- Whisper transcription

Possible engines:

- whisper.cpp
- faster-whisper

Output:

Raw text

---

## Corrector

Responsibilities:

- Hotword correction
- Technical term correction

Examples:

Waze -> Whisper
VS coat -> VS Code

---

## Clipboard

Responsibilities:

- Copy text
- Paste text

---

## UI

Responsibilities:

- Menu bar icon
- Settings
- Hotword editor

---

## Future

Optional local LLM:

- Qwen
- Gemma
- Llama

Purpose:

- Grammar correction
- Punctuation
- Technical terminology repair