from pathlib import Path

import sounddevice as sd
import soundfile as sf


SAMPLE_RATE = 16000


def record_audio(output_path: Path, duration_seconds: int = 10):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"开始录音，时长 {duration_seconds} 秒。现在可以说话。")

    audio = sd.rec(
        int(duration_seconds * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
    )

    sd.wait()

    sf.write(output_path, audio, SAMPLE_RATE)

    print(f"录音完成，已保存到：{output_path}")