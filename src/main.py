from pathlib import Path

from recorder import record_audio_until_enter
from transcriber import transcribe_audio
from clipboard import copy_to_clipboard


AUDIO_PATH = Path("recordings/input.wav")


def main():
    record_audio_until_enter(AUDIO_PATH)

    text = transcribe_audio(AUDIO_PATH)

    print("识别结果：")
    print(text)

    copy_to_clipboard(text)

    print("已复制到剪贴板，可以手动 Command + V 粘贴。")


if __name__ == "__main__":
    main()