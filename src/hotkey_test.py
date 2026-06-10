from pynput import keyboard


HOTKEY = keyboard.HotKey(
    keyboard.HotKey.parse("<ctrl>+<alt>+h"),
    lambda: print("全局快捷键触发了！"),
)


def on_press(key):
    HOTKEY.press(key)


def on_release(key):
    HOTKEY.release(key)


with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print("正在监听全局快捷键：Control + Option + H")
    print("按 Ctrl + C 退出。")
    listener.join()