from pathlib import Path

from pynput import keyboard

from dictation_pipeline import process_audio
from recorder import RecordingSession
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
    process_audio(
        AUDIO_PATH,
        model_size=config["model_size"],
        device=config["device"],
        compute_type=config["compute_type"],
        auto_paste=AUTO_PASTE,
    )


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