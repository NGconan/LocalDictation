from pathlib import Path

from pynput import keyboard

from clipboard import copy_to_clipboard
from corrector import correct_hotwords
from paster import paste_from_clipboard
from recorder import RecordingSession
from transcriber import transcribe_audio


AUDIO_PATH = Path("recordings/input.wav")

recording_session = RecordingSession(AUDIO_PATH)


def transcribe_and_paste():
    print("开始识别...")

    text = transcribe_audio(AUDIO_PATH)
    text = correct_hotwords(text)

    print("识别结果：")
    print(text)

    if not text:
        print("没有识别到文字。")
        return

    copy_to_clipboard(text)
    paste_from_clipboard()

    print("已复制到剪贴板，并已尝试自动粘贴。")


def toggle_recording():
    if recording_session.is_recording:
        recording_session.stop()
        transcribe_and_paste()
    else:
        recording_session.start()


HOTKEY = keyboard.HotKey(
    keyboard.HotKey.parse("<ctrl>+<alt>+h"),
    toggle_recording,
)


def on_press(key):
    HOTKEY.press(key)


def on_release(key):
    HOTKEY.release(key)


def main():
    print("LocalDictation 全局快捷键模式已启动。")
    print("按 Control + Option + H 开始录音。")
    print("再次按 Control + Option + H 停止录音并自动粘贴。")
    print("按 Ctrl + C 退出。")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()