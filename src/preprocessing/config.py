

# Location of the folders and subfolders which contain the audio files.
raw_audio_dir: str = "../data/raw-audio"

# Path to the ffmpeg static binary. That is, if we execute the string, it launches ffmpeg directly.
#    FFmpeg contains various audio/visual encoding and decoding formats. To install:
#        1. (Recommended) Download a static binary and place in somewhere: https://johnvansickle.com/ffmpeg/
#        2. Compile from source: https://www.ffmpeg.org/
#    Your FFmpeg binary can be entirely in user-space (i.e., you do not need sudo).
ffmpeg = "../ffmpeg/ffmpeg"