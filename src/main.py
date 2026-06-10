from pathlib import Path

from recorder import record_audio_until_enter
from transcriber import transcribe_audio
from clipboard import copy_to_clipboard
from corrector import correct_hotwords
from paster import paste_from_clipboard


AUDIO_PATH = Path("recordings/input.wav")


def main():
    record_audio_until_enter(AUDIO_PATH)

    text = transcribe_audio(AUDIO_PATH)
    text = correct_hotwords(text)

    print("识别结果：")
    print(text)

    copy_to_clipboard(text)
    paste_from_clipboard()
    print("已复制到剪贴板，并已尝试自动粘贴。")


if __name__ == "__main__":
    main()