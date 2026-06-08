from pathlib import Path

from faster_whisper import WhisperModel


def transcribe_audio(audio_path: Path) -> str:
    print("开始识别...")

    model = WhisperModel("small", device="cpu", compute_type="int8")

    segments, info = model.transcribe(
        str(audio_path),
        language="zh",
    )

    text = "".join(segment.text for segment in segments).strip()

    return text