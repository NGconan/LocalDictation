# LocalDictation Project Plan

## 1. Project Name

**LocalDictation**

A local-first macOS voice input tool powered by Whisper. The goal is to build a simple, private, low-cost alternative to subscription-based voice dictation apps.

The first version should focus on macOS only. iOS can be considered later after the Mac version becomes usable.

## 2. Core Idea

The app should work like this:

```
Press a global hotkey
↓
Record voice
↓
Run local speech-to-text transcription
↓
Post-process the text
↓
Paste the result into the current text field
```

The first version does **not** need to be a real system input method. A global hotkey plus clipboard paste is enough for the MVP.

## 3. Why Build This

Existing voice input apps can be very expensive. Some apps charge close to the cost of a full AI subscription while only providing voice input.

A local version has several advantages:

- No recurring subscription.
- Better privacy.
- Works with personal hotwords and technical vocabulary.
- Can be customized for Chinese-English mixed speech.
- Can be extended later with local LLM correction.
- Can be open-sourced on GitHub.

## 4. MVP Scope

The first usable version should include only the essentials.

### MVP Features

- Record audio from the microphone.
- Save temporary audio to a local file.
- Run local Whisper transcription.
- Copy transcribed text to clipboard.
- Paste the text into the currently active app.
- Support a simple hotkey workflow.
- Keep everything local.

### Not Included in MVP

- Real iOS support.
- Real macOS input method extension.
- Full GUI settings page.
- Cloud sync.
- Account system.
- Subscription system.
- Advanced AI rewriting.
- Real-time streaming transcription.

## 5. Suggested Development Strategy

Start with a Python prototype first. Do not start with Swift immediately.

The goal of the Python prototype is to prove that the full workflow works:

```
Record audio → transcribe → copy → paste
```

After that, rebuild it as a native macOS app if the prototype feels useful.

## 6. Phase 1: Project Setup

Create the project folder:

```
mkdir LocalDictation
cd LocalDictation
mkdir src models recordings scripts docs
touch README.md PROJECT_PLAN.md
```

Suggested structure:

```
LocalDictation/
├── README.md
├── PROJECT_PLAN.md
├── src/
├── models/
├── recordings/
├── scripts/
└── docs/
```

## 7. Phase 2: Run Whisper Locally

There are two main options.

### Option A: whisper.cpp

Best for local performance and future native app integration.

Repository:

```
https://github.com/ggml-org/whisper.cpp
```

Pros:

- Fast.
- Good for Apple Silicon.
- Can run fully offline.
- Suitable for later Swift/macOS integration.

Cons:

- Requires compiling or installing binaries.
- Slightly more setup work.

### Option B: Python Whisper / Faster-Whisper

Best for fast prototyping.

Pros:

- Easy to test.
- Good for early MVP.
- Easier to integrate in Python.

Cons:

- Less elegant for a polished native macOS app.
- Python environment management can get messy.

Recommended first step:

```
Use Python first if the goal is to learn and prototype quickly.
Move to whisper.cpp later for the native version.
```

## 8. Phase 3: Basic Audio Recording

Start with a simple command-line script.

First version behavior:

```
Run script
↓
Press Enter to start recording
↓
Press Enter again to stop recording
↓
Save recording to recordings/input.wav
```

Possible Python libraries:

```
sounddevice
soundfile
```

The purpose of this phase is only to get a valid audio file.

No hotkey yet.

No GUI yet.

No automatic paste yet.

## 9. Phase 4: Transcription Pipeline

After recording works, connect the audio file to Whisper.

Pipeline:

```
recordings/input.wav
↓
Whisper transcription
↓
raw text output
```

Example output:

```
我今天想测试一下 Whisper 的本地语音输入效果。
```

At this stage, simply print the result in Terminal.

## 10. Phase 5: Clipboard and Paste

After transcription works, copy the recognized text to the clipboard.

Then simulate:

```
Command + V
```

This turns the prototype into a usable voice input tool.

Possible tools:

- Python clipboard library.
- AppleScript.
- macOS accessibility automation.
- `pbcopy`.
- `osascript`.

Simple first approach:

```
echo "recognized text" | pbcopy
```

Then paste manually.

Later:

```
Automatically trigger Command + V
```

## 11. Phase 6: Global Hotkey

After the basic workflow works, add a global hotkey.

Target behavior:

```
Hold Option + Space
↓
Speak
↓
Release keys
↓
Transcribe
↓
Paste
```

Simpler early behavior:

```
Press Option + Space once to start
Press Option + Space again to stop
```

The toggle version is easier than press-and-hold.

For the Python prototype, use any library that can listen for global shortcuts on macOS.

For the native version, use Swift and macOS event handling.

## 12. Phase 7: Hotword Correction

This is very important for the user.

Create a file:

```
hotwords.txt
```

Example content:

```
Whisper
OpenAI
ChatGPT
GPT-5
Ollama
Xray
VLESS
Reality
Sing-box
VS Code
Codex
GitHub
CRA
Fomapan
D-76
LQR
```

Use this file to correct common mistakes.

Example:

```
Waze → Whisper
X read → Xray
really tea → Reality
VS coat → VS Code
```

This can start as simple string replacement.

Later it can become smarter.

## 13. Phase 8: Local LLM Post-Processing

After Whisper works, add optional correction using a local LLM.

Example model:

```
Qwen
Llama
Gemma
```

Possible local backend:

```
Ollama
```

Post-processing prompt idea:

```
Correct transcription errors, punctuation, capitalization, and technical terms.
Do not change the meaning.
Preserve the user's original language and tone.
```

Example:

Raw Whisper output:

```
我刚才用 waze 做语音识别
```

Corrected output:

```
我刚才用 Whisper 做语音识别。
```

This step should be optional because it adds latency.

## 14. Phase 9: Native macOS App

After the Python MVP works, build a proper macOS app.

Recommended stack:

```
Swift
SwiftUI
AVFoundation
whisper.cpp
Accessibility API
Menu bar app
```

Native Mac app features:

- Menu bar icon.
- Start/stop recording.
- Global hotkey.
- Local model selection.
- Hotword list editor.
- Clipboard paste.
- Optional sound feedback.
- Optional text preview before paste.

## 15. Phase 10: iOS Version

iOS should come later.

Possible approaches:

### Approach A: Standalone App

User opens the app, records speech, copies result.

Pros:

- Easier.
- Less system restriction.

Cons:

- Not as convenient as a true keyboard.

### Approach B: Keyboard Extension

User can use it inside any app like a real input method.

Pros:

- Best user experience.

Cons:

- Much harder.
- iOS sandbox restrictions.
- Microphone access and model loading may be tricky.
- Large local models may be inconvenient.
- Background behavior is limited.

Recommended path:

```
Do not start with iOS.
Finish Mac first.
```

## 16. Privacy Philosophy

The project should be local-first.

Default behavior:

```
Audio stays on device.
Text stays on device.
No account.
No cloud upload.
No tracking.
No subscription.
```

If cloud features are ever added, they should be optional.

## 17. GitHub Positioning

Possible GitHub description:

```
A local-first macOS voice dictation tool powered by Whisper.
Press a hotkey, speak, transcribe locally, and paste anywhere.
```

Possible README tagline:

```
Local voice input without subscriptions.
```

Possible target users:

- Developers.
- Bilingual Chinese-English users.
- People who use technical vocabulary.
- Users who dislike expensive dictation subscriptions.
- Users who want privacy-friendly speech input.

## 18. Development Milestones

### Milestone 0: Project folder

- Create repository.
- Add README.
- Add PROJECT_PLAN.md.
- Add basic folder structure.

### Milestone 1: Audio recording

- Record microphone audio.
- Save as WAV.

### Milestone 2: Whisper transcription

- Run local transcription.
- Print result in Terminal.

### Milestone 3: Clipboard output

- Copy transcribed text to clipboard.

### Milestone 4: Manual paste workflow

- User can paste text manually after transcription.

### Milestone 5: Auto paste

- Automatically paste into current app.

### Milestone 6: Global hotkey

- Start/stop dictation with shortcut.

### Milestone 7: Hotword correction

- Add custom vocabulary.
- Fix common recognition mistakes.

### Milestone 8: Local LLM cleanup

- Optional grammar and punctuation correction.

### Milestone 9: Native macOS app

- Menu bar app.
- Settings.
- Model selection.

### Milestone 10: iOS exploration

- Evaluate standalone app vs keyboard extension.

## 19. Important Design Principle

Do not overbuild the first version.

The first successful version only needs to do this:

```
Record → transcribe → paste
```

Everything else can come later.

## 20. Immediate Next Step

Start with this:

```
Create a Python script that records 10 seconds of audio and saves it as WAV.
```

Then:

```
Run Whisper on that WAV file and print the result.
```

Once that works, the project is real.