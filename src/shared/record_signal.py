import sounddevice as sd
import soundfile as sf
from numpy import ndarray

def convert_audio_to_numpy_array(recording_path: str):
    data, samplerate = sf.read(recording_path, dtype='float32')
    return data, samplerate
    
def record_sound(duration: int, samplerate: int, channel_count: int):
    return sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channel_count)

def play_sound(recording: ndarray, samplerate: int):
    sd.play(recording, samplerate)

def play_and_record(recording, samplerate: int, channels: int):
    return sd.playrec(recording, samplerate, channels, dtype='float64')

