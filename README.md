# yt2mp4

Download YouTube videos as MP4 files (and other formats)

## Get geckodriver

### Linux (Debian)

```sh
sudo apt install firefox-geckodriver -y
```

### Other

Figure it yourself

## Installation

### From PyPI

```sh
pip3 install yt2mp4
```

### From GitHub

```sh
pip3 install git+https://github.com/donno2048/yt2mp4
```

## Usage

### In Python

```py
from yt2mp4 import download
download("dQw4w9WgXcQ", outname='output.mp4') # dowload video from https://www.youtube.com/watch?v=dQw4w9WgXcQ and name it output.mp4
# will also work:
# download("https://www.youtube.com/watch?v=dQw4w9WgXcQ", output="output.mov")
# download("https://youtu.be/dQw4w9WgXcQ")
```

### In cmd

```sh
yt2mp4 # or python3 -m yt2mp4
# yt2webm
# yt2mkv
# yt2flv
# yt2wmv
# yt2avi
# yt2mov
# yt2m4v
# yt2mp3
```

## Supported formats

- mp4
- webm
- mkv
- flv
- wmv
- avi
- mov
- m4v
- mp3 (auto format as audio)
