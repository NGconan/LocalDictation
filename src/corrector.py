HOTWORD_REPLACEMENTS = {
    "VS coat": "VS Code",
    "VS Cota": "VS Code",
    "VS cota": "VS Code",
    "v s code": "VS Code",
    "open AI": "OpenAI",
}


def correct_hotwords(text: str) -> str:
    for wrong, correct in HOTWORD_REPLACEMENTS.items():
        text = text.replace(wrong, correct)

    return text