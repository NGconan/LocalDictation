from faster_whisper import WhisperModel


_model = None
_model_config = None


def get_model(model_size: str, device: str, compute_type: str):
    global _model
    global _model_config

    current_config = (model_size, device, compute_type)

    if _model is None or _model_config != current_config:
        print(f"正在加载 Whisper 模型：{model_size}, device={device}, compute_type={compute_type}")
        _model = WhisperModel(model_size, device=device, compute_type=compute_type)
        _model_config = current_config

    return _model


def transcribe_audio(
    audio_path,
    model_size: str = "small",
    device: str = "cpu",
    compute_type: str = "int8",
) -> str:
    model = get_model(model_size, device, compute_type)

    segments, info = model.transcribe(audio_path)

    text_parts = []

    for segment in segments:
        text_parts.append(segment.text)

    return "".join(text_parts).strip()