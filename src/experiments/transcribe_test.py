from faster_whisper import WhisperModel

AUDIO_PATH = "recordings/input.wav"


def main():
    model = WhisperModel("small", device="cpu", compute_type="int8")

    segments, info = model.transcribe(
        AUDIO_PATH,
        language="zh",
    )

    print("识别结果：")

    for segment in segments:
        print(segment.text)


if __name__ == "__main__":
    main()