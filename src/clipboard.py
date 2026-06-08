import subprocess


def copy_to_clipboard(text: str):
    subprocess.run("pbcopy", text=True, input=text)