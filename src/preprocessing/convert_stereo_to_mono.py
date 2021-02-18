import os
import string
import argparse
import subprocess
import multiprocessing
from typing import Tuple
import config

def main(args: argparse.Namespace):
    """Handles high-level filename collection, directory creation, and thread management."""
    # Create the output directory, if it does not exist.
    print("Creating the output directory...")
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    else:
        print("Output directory already exists.")

    # Recursively get list of all audio filenames and their desired output filename.
    workload = []
    print("Gathering input filenames...")
    for path, _, filenames in os.walk(config.raw_audio_dir):
        for filename in filenames:
            # Get the base filename without the audio extension.
            basename = ".".join(filename.split(".")[:-1])
            source_fqn = os.path.join(config.raw_audio_dir, filename)  # fqn: Fully-qualified name.
            dest_fqn = os.path.join(args.output_dir, f"{basename}.flac")

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
    Converts a single audio file `source_fqn` into a flac file and saves it to `dest_fqn`.
    :param item: Tuple containing two strings: source_fqn and dest_fqn.
        source_fqn: Absolute filename of the source audio.
        dest_fqn: Absolute filename of the destination flac file.
    """
    source_fqn, dest_fqn = item
    # -i = input, -c:a = audio codec, -ac = # output channels, -ar = output sampling rate
    # -af "pan=mono|c0=c1" = split channel (convert stereo to mono)
    # Note that Google recommends 16,000 Hz. This is because their models are trained on 16,000.
    # Anything higher (e.g. 44kHz) significantly increases the filesize without any performance gains.
    cmd_template = string.Template(
        f'{config.ffmpeg} -i "$source" -af "pan=mono|c0=c1" -ac 1 -c:a flac -ar 8000 "$dest"'
    )
    cmd = cmd_template.substitute(source=source_fqn, dest=dest_fqn)

    # Execute on command line.
    subprocess.run(cmd, shell=True)

# Example command: python convert_stereo_to_mono.py ../output/
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "output_dir",
        type=str,
        help="Location where to place the new flac files.",
    )
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