import subprocess
from faster_whisper import WhisperModel

AUDIO_PATH = "recordings/input.wav"


def copy_to_clipboard(text: str):
    subprocess.run("pbcopy", text=True, input=text)


def main():
    model = WhisperModel("small", device="cpu", compute_type="int8")

    segments, info = model.transcribe(
        AUDIO_PATH,
        language="zh",
    )

    text = "".join(segment.text for segment in segments).strip()

    print("识别结果：")
    print(text)

    copy_to_clipboard(text)
    print("已复制到剪贴板，可以手动 Command + V 粘贴。")


if __name__ == "__main__":
    main()