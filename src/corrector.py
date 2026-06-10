from pathlib import Path


HOTWORDS_PATH = Path("hotwords.txt")


def load_hotword_replacements(hotwords_path: Path = HOTWORDS_PATH) -> dict[str, str]:
    replacements = {}

    if not hotwords_path.exists():
        return replacements

    with hotwords_path.open("r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()

            if not line:
                continue

            if line.startswith("#"):
                continue

            if "=>" not in line:
                continue

            wrong, correct = line.split("=>", 1)

            wrong = wrong.strip()
            correct = correct.strip()

            if wrong and correct:
                replacements[wrong] = correct

    return replacements


def correct_hotwords(text: str) -> str:
    replacements = load_hotword_replacements()

    for wrong, correct in replacements.items():
        text = text.replace(wrong, correct)

    return text
