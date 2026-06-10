# 嗲用math数学库
import math
#调用pathlib中的path 类用于处理文件路径
from pathlib import Path
#调用sounddevice库用于录音并缩写为sd
import sounddevice as sd
#调用soundfile如用于保存录音并缩写为sf
import soundfile as sf
import numpy as np
import threading

#定义常量 SAMPLE_RATE用于设置为 16000Hz 的采样率，whisper 模型使用这个采样率足够语音识别并减少资源占用
SAMPLE_RATE = 16000

#定义函数 record_audio 用于录音并保存到指定路径，参数 output_path 是一个 path 输出路径，duration_seconds 是录音时间单位是秒，提示建议使用 float 型
def record_audio(output_path: Path, duration_seconds: float):
    # 检查 duration_seconds 是否大于 0，如果不是就抛出 ValueError 异常
    if duration_seconds <= 0:
        raise ValueError("duration_seconds must be greater than 0")
#确认输出目录存在如果不存在则用 mkdir创建目录
# parent 返回 output_path 的父目录，parents=True 递归创建父目录
#exist_ok=True 如果目录已存在咱不报错
    output_path.parent.mkdir(parents=True, exist_ok=True)

#定义变量frames用于计算录音总帧数，用过数学库中的ceil函数向上取整，计算公式为录音时间乘以采样率
    frames = math.ceil(duration_seconds * SAMPLE_RATE)

#输出提示信息告诉用户录音开始和持续时间，并提示用户现在可以说话了
    print(f"开始录音，时长 {duration_seconds} 秒。现在可以说话。")
#调用sounddevice 库中的 rec 函数开始录音
    audio = sd.rec(
        frames, #总帧数
        samplerate=SAMPLE_RATE, #采样率
        channels=1, #单声道
        dtype="float32", #数据类型为 32 位浮点数适合音频处理
    )

    sd.wait() #等待录音完成
#调用soundfile库中的write函数将录音保存到指定路径，参数包括输出路径，音频数据和采样率
    sf.write(output_path, audio, SAMPLE_RATE)
#最后输出提示信息告诉用户录音完成并显示保存路径
    print(f"录音完成，已保存到：{output_path}")

def record_audio_until_enter(output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    audio_chunks = []

    def audio_callback(indata, frames, time, status):
        if status:
            print(status)

        audio_chunks.append(indata.copy())

    input("按 Enter 开始录音。")

    print("开始录音。说完后再按 Enter 停止。")

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        callback=audio_callback,
    ):
        input()

    if not audio_chunks:
        raise RuntimeError("没有录到音频。")

    audio = np.concatenate(audio_chunks, axis=0)

    sf.write(output_path, audio, SAMPLE_RATE)

    print(f"录音完成，已保存到：{output_path}")

class RecordingSession:
    def __init__(self, output_path: Path):
        self.output_path = output_path
        self.audio_chunks = []
        self.stream = None
        self.is_recording = False

    def _audio_callback(self, indata, frames, time, status):
        if status:
            print(status)

        self.audio_chunks.append(indata.copy())

    def start(self):
        if self.is_recording:
            print("已经在录音中。")
            return

        self.output_path.parent.mkdir(parents=True, exist_ok=True)
        self.audio_chunks = []

        self.stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=1,
            dtype="float32",
            callback=self._audio_callback,
        )

        self.stream.start()
        self.is_recording = True
        print("开始录音。再次按快捷键停止。")

    def stop(self):
        if not self.is_recording:
            print("当前没有在录音。")
            return

        self.stream.stop()
        self.stream.close()
        self.stream = None
        self.is_recording = False

        if not self.audio_chunks:
            raise RuntimeError("没有录到音频。")

        audio = np.concatenate(self.audio_chunks, axis=0)
        sf.write(self.output_path, audio, SAMPLE_RATE)

        print(f"录音完成，已保存到：{self.output_path}")