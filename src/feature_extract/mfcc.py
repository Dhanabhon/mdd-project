import os
import argparse
import librosa

def main(args):
    
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    else:
        print("Output directory already exists.")
    
    x, sr = librosa.load()
    print(type(x), type(sr))



if __name__ == "__main_":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_dir",
        type=str,
        help="Location where to place the spectrogram picture files."        
    )

    args = parser.parse_args()
    main(args)