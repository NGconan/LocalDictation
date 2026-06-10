from pathlib import Path

from clipboard import copy_to_clipboard
from corrector import correct_hotwords
from paster import paste_from_clipboard
from transcriber import transcribe_audio


def process_audio(
    audio_path: Path,
    model_size: str,
    device: str,
    compute_type: str,
    auto_paste: bool,
) -> str:
    print("开始识别...")

    text = transcribe_audio(
        audio_path,
        model_size=model_size,
        device=device,
        compute_type=compute_type,
    )

    text = correct_hotwords(text)

    print("识别结果：")
    print(text)

    if not text:
        print("没有识别到文字。")
        return text

    copy_to_clipboard(text)

    if auto_paste:
        paste_from_clipboard()
        print("已复制到剪贴板，并已尝试自动粘贴。")
    else:
        print("已复制到剪贴板。")

    return text