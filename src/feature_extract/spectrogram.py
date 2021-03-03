import os
import librosa
import numpy as np
import config

def stft(signal, frame_size, overlap_fac=0.5, window=np.hanning):
    win = window(frame_size)
    hop_length = int(frame_size - np.floor(overlap_fac * frame_size))

    stft = librosa.core.stft(signal, n_fft=frame_size, hop_length=hop_length)
    spectrogram = np.abs(stft)


def stft_matrix(audio_path, bin_size=1024, png_name='tmp.png', save_png=False, offset=0):
    signal, sr = librosa.load(audio_path, sr=8000)

    # show, freq = logscale_spec(s, factor=1, sr=sr)
    # ims = 20.0 * np.log10(np.abs())


if __name__ == '__main__':
    for subdir, dirs, files in os.walk(config.output_audio_dir):
        for file in files:
            if file.endswith('.flac'):
                flac_file = os.path.join(subdir, file)
                png_name = subdir + '/' + file[:-4] + '.png'
                print("Processing " + file + "...")
                
