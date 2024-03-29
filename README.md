# Automated Speech-Based Screening of Depression Using Machine Learning Approaches

![Logo Image](pics/communication.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://tldrlegal.com/license/mit-license)
[![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)](https://www.python.org/downloads/release/python-385)

First, install the python dependencies.
```bash
pip install -r requirements.txt
```

## 1. Data Preprocessing

[Return to top](#automated-speech-based-screening-of-depression-using-machine-learning-approaches)

### 1.1. Prerequisites
[FFmpeg](https://www.ffmpeg.org) contains various audio/visual encoding and decoding formats. To install FFmpeg:

1. (Recommended) Download a static binary and place in home dir: [https://johnvansickle.com/ffmpeg](https://johnvansickle.com/ffmpeg)
2. Compile from source: [https://www.ffmpeg.org](https://www.ffmpeg.org)

Your FFmpeg binary can be entirely in user-space (i.e., you do not need sudo).

[SoX](http://sox.sourceforge.net/) is a cross-platform (Windows, Linux, and macOS) command line utility that can convert various formats of computer audio files in to other formats. To install SoX: 
- [Windows](https://github.com/JoFrhwld/FAVE/wiki/Sox-on-Windows)

### 1.2. Generating FLAC Files and manipulating audio channels (audio filter to include only the right channel)
In its raw form, our current audio files are in either WMA (windows media audio) or MP3 format.

Below, we show the original (mp3/wma) specs of our data and the specs of our new FLAC files.

* Format: MP3/WMA -> FLAC
* Sample Rate: 8,000 Hz
* Channels: 2 (stereo) -> 1 (mono)

First, open [preprocessing/config.py](preprocessing/config.py) and edit the variables: `raw_audio_dir`, `ffmpeg`, as appropriate. 
<!--[preprocessing/convert_stereo_to_mono.py](preprocessing/convert_stereo_to_mono.py) and edit the global variables: `INPUT_DIR`, `OUTPUT_DIR`, and `ffmpeg`. -->
Then, run:

```bash
python preprocessing/convert_stereo_to_mono.py [OUTPUT_DIR]
```
The output flac files will be placed in `OUTPUT_DIR`.

## 2. Feature Extraction
Coming Soon...

## 3. An Automated Speech-Based Screening of Depression Framework
Coming Soon...

[Return to top](#automated-speech-based-screening-of-depression-using-machine-learning-approaches)

## Credits
Icons made by Freepik from www.flaticon.co
