from pathlib import Path

from pynput import keyboard

from clipboard import copy_to_clipboard
from corrector import correct_hotwords
from paster import paste_from_clipboard
from recorder import RecordingSession
from transcriber import transcribe_audio
from config import load_config


try:
    config = load_config()
except ValueError as error:
    print("配置文件错误：")
    print(error)
    raise SystemExit(1)

AUDIO_PATH = Path(config["audio_path"])
HOTKEY_TEXT = config["hotkey"]
AUTO_PASTE = config["auto_paste"]

recording_session = RecordingSession(AUDIO_PATH)


def transcribe_and_paste():
    print("开始识别...")

    text = transcribe_audio(
    AUDIO_PATH,
    model_size=config["model_size"],
    device=config["device"],
    compute_type=config["compute_type"],
)
    text = correct_hotwords(text)

    print("识别结果：")
    print(text)

    if not text:
        print("没有识别到文字。")
        return

    copy_to_clipboard(text)

    if AUTO_PASTE:
        paste_from_clipboard()
        print("已复制到剪贴板，并已尝试自动粘贴。")
    else:
        print("已复制到剪贴板。")


def toggle_recording():
    try:
        if recording_session.is_recording:
            recording_session.stop()
            transcribe_and_paste()
        else:
            recording_session.start()
    except Exception as error:
        print("处理过程中出错：")
        print(error)


HOTKEY = keyboard.HotKey(
    keyboard.HotKey.parse(HOTKEY_TEXT),
    toggle_recording,
)


def on_press(key):
    HOTKEY.press(key)


def on_release(key):
    HOTKEY.release(key)


def main():
    print("LocalDictation 全局快捷键模式已启动。")
    print(f"按 {HOTKEY_TEXT} 开始录音。")
    print(f"再次按 {HOTKEY_TEXT} 停止录音并自动粘贴。")
    print("按 Ctrl + C 退出。")

    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


if __name__ == "__main__":
    main()