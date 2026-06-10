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


ALLOWED_MODEL_SIZES = {
    "tiny",
    "base",
    "small",
    "medium",
    "large-v1",
    "large-v2",
    "large-v3",
}


ALLOWED_DEVICES = {
    "cpu",
    "cuda",
    "auto",
}


ALLOWED_COMPUTE_TYPES = {
    "int8",
    "int8_float16",
    "int16",
    "float16",
    "float32",
    "default",
}


def validate_config(config: dict) -> None:
    if not isinstance(config["hotkey"], str):
        raise ValueError("config.json 里的 hotkey 必须是字符串。")

    if not config["hotkey"].strip():
        raise ValueError("config.json 里的 hotkey 不能为空。")

    if config["model_size"] not in ALLOWED_MODEL_SIZES:
        raise ValueError(
            f"config.json 里的 model_size 不支持：{config['model_size']}。"
            f"可选值：{sorted(ALLOWED_MODEL_SIZES)}"
        )

    if config["device"] not in ALLOWED_DEVICES:
        raise ValueError(
            f"config.json 里的 device 不支持：{config['device']}。"
            f"可选值：{sorted(ALLOWED_DEVICES)}"
        )

    if config["compute_type"] not in ALLOWED_COMPUTE_TYPES:
        raise ValueError(
            f"config.json 里的 compute_type 不支持：{config['compute_type']}。"
            f"可选值：{sorted(ALLOWED_COMPUTE_TYPES)}"
        )

    if not isinstance(config["audio_path"], str):
        raise ValueError("config.json 里的 audio_path 必须是字符串。")

    if not config["audio_path"].strip():
        raise ValueError("config.json 里的 audio_path 不能为空。")

    if not isinstance(config["auto_paste"], bool):
        raise ValueError("config.json 里的 auto_paste 必须是 true 或 false。")


def load_config(config_path: Path = CONFIG_PATH) -> dict:
    if not config_path.exists():
        config = DEFAULT_CONFIG.copy()
        validate_config(config)
        return config

    try:
        with config_path.open("r", encoding="utf-8") as file:
            user_config = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError(f"config.json 格式错误：{error}") from error

    if not isinstance(user_config, dict):
        raise ValueError("config.json 最外层必须是一个 JSON object，也就是用 { } 包起来。")

    config = DEFAULT_CONFIG.copy()
    config.update(user_config)

    validate_config(config)

    return config