import subprocess


def paste_from_clipboard():
    script = '''
    tell application "System Events"
        keystroke "v" using command down
    end tell
    '''

    subprocess.run(["osascript", "-e", script])