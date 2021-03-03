import os
import argparse
import librosa, librosa.display
import matplotlib.pyplot as plt
import numpy as np
import config

def main(args: argparse.Namespace):
    # Create the output directory, if it does not exist.
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    else:
        print("Output directory already exists.")

    # Recursively get list of all audio filenames and their desired output filename.
    workload = []
    print("Gathering input filenames...")
    for path, _, filenames in os.walk(config.output_audio_dir):
        for filename in filenames:
            source_fqn = os.path.join(config.output_audio_dir, filename)
            workload.append((source_fqn))

            print(source_fqn)
            # Waveform
            signal, sr = librosa.load(source_fqn, sr=8000)
            librosa.display.waveplot(signal, sr=sr)
            plt.xlabel("Time")
            plt.ylabel("Amplitude")
            plt.show()

            # FFT -> spectrum
            fft = np.fft.fft(signal)
            magnitude = np.abs(fft)
            frequency = np.linspace(0, sr, len(magnitude))

            left_frequency = frequency[:int(len(frequency) / 2)]
            left_magnitude = magnitude[:int(len(frequency) / 2)]

            plt.plot(left_frequency, left_magnitude)
            plt.xlabel("Frequency")
            plt.ylabel("Magnitude")
            plt.show()

            # STFT -> Spectrogram
            n_fft = 2048
            hop_length = 512
            stft = librosa.core.stft(signal, n_fft=n_fft, hop_length=hop_length)
            spectrogram = np.abs(stft)

            log_spectrogram = librosa.amplitude_to_db(spectrogram)

            librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
            plt.xlabel("Time")
            plt.ylabel("Frequency")
            plt.colorbar()
            plt.show()

            # MFCCs
            mfcc = librosa.feature.mfcc(signal, sr=sr, n_mfcc=13)
            librosa.display.specshow(mfcc, sr=sr, hop_length=hop_length)
            plt.xlabel("Time")
            plt.ylabel("MFCC")
            plt.colorbar()
            plt.show()
        
        # print(path)

    print(f"Found {len(workload)} files.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_dir",
        type=str,
        help="Location where to place the spectrogram picture files."        
    )

    args = parser.parse_args()
    main(args)