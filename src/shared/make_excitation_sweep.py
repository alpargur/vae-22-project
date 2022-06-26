import numpy as np
from scipy.signal import chirp

def make_excitation_sweep(fs, num_channels=1, d_sweep_sec=3, d_post_silence_sec=1, f_start=20, f_end=20000, amp_db=-20, fade_out_samples=0):

    amplitude_lin = 10 ** (amp_db / 20)

    # make sweep
    t_sweep = np.linspace(0, d_sweep_sec, int(d_sweep_sec * fs))
    sweep = amplitude_lin * chirp(t_sweep, f0=f_start, t1=d_sweep_sec, f1=f_end, method='logarithmic', phi=90)

    # squared cosine fade
    fade_tmp = np.cos(np.linspace(0, np.pi / 2, fade_out_samples)) ** 2
    window = np.ones(np.size(sweep, 0))
    window[np.size(window) - fade_out_samples: np.size(window)] = fade_tmp
    sweep = sweep * window

    pre_silence = int(fs * 0.01) # 10msec post silence for safety while playback
    post_silence = int(fs * d_post_silence_sec)


    excitation = np.pad(sweep, (pre_silence, post_silence))

    excitation = np.tile(excitation, (num_channels, 1))  # make stereo or more, for out channels 1 & 2
    excitation = np.transpose(excitation).astype(np.float32)

    return excitation