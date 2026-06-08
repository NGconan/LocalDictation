import sounddevice as sd
import soundfile as sf
from pathlib import Path

SAMPLE_RATE = 16000
DURATION_SECONDS = 10
OUTPUT_PATH = Path("recordings/input.wav")


def main():
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)

    print("开始录音，时长 10 秒。现在可以说话。")

    audio = sd.rec(
        int(DURATION_SECONDS * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    sf.write(OUTPUT_PATH, audio, SAMPLE_RATE)

    print(f"录音完成，已保存到：{OUTPUT_PATH}")


if __name__ == "__main__":
    main()