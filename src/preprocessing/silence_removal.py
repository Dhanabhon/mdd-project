import os
import string
import argparse
import subprocess
import multiprocessing
from typing import Tuple

import config

def main(args: argparse.Namespace):
    # Create the output directory, if it does not exist.
    print("Creating the output directory...")
    if not os.path.exists(config.audio_nomalized_silence_removed_dir):
        os.makedirs(config.audio_nomalized_silence_removed_dir)
    else:
        print("Audio output directory already exists.")
    
    # Recursively get list of all audio filenames and their desired output filename.
    workload = []
    print("Gathering input filenames...")
    for path, _, filenames in os.walk(config.audio_nomalized_output_dir):
        for filename in filenames:
            # Get the base filename without the audio extension.
            basename = ".".join(filename.split(".")[:-1])

            # fqn: Fully-qualified name.
            source_fqn = os.path.join(path, filename) 
            dest_fqn = os.path.join(config.audio_nomalized_silence_removed_dir, f"{basename}.flac")

            # If we're continuing an interrupted job, we should skip any completed files.
            if args.resume:
                if os.path.exists(dest_fqn):
                    continue
            workload.append((source_fqn, dest_fqn))
    print(f"Found {len(workload)} files.")

    # Create multiple threads.
    print(f"Starting {args.n_threads} threads...")
    with multiprocessing.Pool(args.n_threads) as pool:
        pool.map(worker, workload)

def worker(item: Tuple[str, str]):
    """
    Converts a single audio file `souce_fqn` into a flac file and saves it to `dest_fqn`.
    :parameter item: Tuple containing two strings: source_fqn and dest_fqn.
        source_fqn: Absolute filename of the sourcee audio.
        dest_fqn: Absolute filename of the destination flac file.
    """
    source_fqn, dest_fqn = item
    
    # ffmpeg -i INPUT.mp3 -af silencedetect=n=-50dB:d=1
    # cmd_template = string.Template(
    #     f'{config.ffmpeg} -i "$source" -af silenceremove=stop_periods=-1:stop_duration=1:stop_threshold=-90dB "$dest"'
    # )

    cmd_template = string.Template(
        "sox $source $dest silence -l 1 0.1 1% -1 0.1 1%"
    )

    cmd = cmd_template.substitute(source=source_fqn, dest=dest_fqn)
    # Execute on command line.
    subprocess.run(cmd, shell=True)

# Execute command: python silence_removal.py --n_threads=1
if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--n_threads",
        default=1,
        type=int,
        help="Number of simultaneous FFmpeg calls. Note, all available threads are always used.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="If True, skip files already completed. Useful for resuming an interrupted job.",
    )

    args = parser.parse_args()
    main(args)
    