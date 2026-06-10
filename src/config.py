import json
from pathlib import Path


CONFIG_PATH = Path("config.json")


DEFAULT_CONFIG = {
    "hotkey": "<ctrl>+<alt>+h",
    "model_size": "small",
    "device": "cpu",
    "compute_type": "int8",
    "audio_path": "recordings/input.wav",
    "auto_paste": True,
}


def load_config(config_path: Path = CONFIG_PATH) -> dict:
    if not config_path.exists():
        return DEFAULT_CONFIG.copy()

    with config_path.open("r", encoding="utf-8") as file:
        user_config = json.load(file)

    config = DEFAULT_CONFIG.copy()
    config.update(user_config)

    return config