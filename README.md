
# LocalDictation

A local-first macOS voice dictation prototype powered by Whisper.

Current flow:

1. Press Enter to start recording
2. Press Enter again to stop recording
3. Transcribe audio locally with Whisper
4. Apply hotword corrections from `hotwords.txt`
5. Copy the result to clipboard
6. Automatically paste with Command + V

## Requirements

- macOS
- Python 3.10+
- Microphone permission
- Accessibility permission for automatic paste

## Setup

Create and activate a virtual environment:

```Bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```Bash
pip install sounddevice soundfile faster-whisper numpy
```
Usage

Run:

```Bash
python src/main.py
```

Then:

Put your cursor in any text input field
Press Enter in the terminal to start recording
Speak
Press Enter again to stop recording
The recognized text will be copied and pasted automatically
Hotword corrections

Edit hotwords.txt to add correction rules:

```Text
VS Cota => VS Code
VS coat => VS Code
v s code => VS Code
open AI => OpenAI
```

Format:

```teext
wrong text => corrected text
```

Notes

This is currently a Python prototype, not a packaged macOS app.

The automatic paste feature uses macOS automation to simulate Command + V.
If it does not work, enable Accessibility permission for VS Code or Terminal in:

System Settings → Privacy & Security → Accessibility
## Roadmap

- [x] Audio recording
- [x] Whisper integration
- [x] Clipboard output
- [ ] Global hotkey
- [x] Hotword correction
- [ ] Local LLM cleanup
- [ ] Native macOS app
- [ ] iOS exploration

## License

TBD