import subprocess
from pathlib import Path

import sounddevice as sd
import soundfile as sf
from faster_whisper import WhisperModel


SAMPLE_RATE = 16000
DURATION_SECONDS = 10
AUDIO_PATH = Path("recordings/input.wav")


def record_audio():
    AUDIO_PATH.parent.mkdir(parents=True, exist_ok=True)

    print(f"开始录音，时长 {DURATION_SECONDS} 秒。现在可以说话。")

    audio = sd.rec(
        int(DURATION_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    sf.write(AUDIO_PATH, audio, SAMPLE_RATE)

    print(f"录音完成，已保存到：{AUDIO_PATH}")


def transcribe_audio() -> str:
    print("开始识别...")

    model = WhisperModel("small", device="cpu", compute_type="int8")

    segments, info = model.transcribe(
        str(AUDIO_PATH),
        language="zh",
    )

    text = "".join(segment.text for segment in segments).strip()

    return text


def copy_to_clipboard(text: str):
    subprocess.run("pbcopy", text=True, input=text)


def main():
    record_audio()

    text = transcribe_audio()

    print("识别结果：")
    print(text)

    copy_to_clipboard(text)

    print("已复制到剪贴板，可以手动 Command + V 粘贴。")


if __name__ == "__main__":
    main()