# yt2mp4

Download YouTube videos and playlists as MP4 files (and other formats)

## Get geckodriver

### Linux (Debian)

```sh
sudo apt install wget ffmpeg firefox-esr -y
wget https://github.com/mozilla/geckodriver/releases/download/v0.30.0/geckodriver-v0.30.0-linux64.tar.gz
sudo tar xvzf geckodriver-v0.30.0-linux64.tar.gz -C /usr/bin/
chmod +x /usr/bin/geckodriver
rm geckodriver-v0.30.0-linux64.tar.gz
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
# download("dQw4w9WgXcQ", outname='output.mp4', binary_path=path) # use a different binary path
# download("youtube.com/watch?v=dQw4w9WgXcQ", output="output.mov")
# download("youtu.be/dQw4w9WgXcQ")
# download("www.youtube.com/watch?v=dQw4w9WgXcQ", output="output.mov")
# download("music.youtube.com/watch?v=dQw4w9WgXcQ", output="output.mov")
# download("https://www.youtube.com/watch?v=dQw4w9WgXcQ", output="output.mov")
# download("https://music.youtube.com/watch?v=dQw4w9WgXcQ", output="output.mov")
# download("https://youtu.be/dQw4w9WgXcQ")
```

### In cmd

```sh
# each of those will convert to another format
yt2mp4 # or python3 -m yt2mp4
yt2webm
yt2mkv
yt2flv
yt2wmv
yt2avi
yt2mov
yt2m4v
yt2mp3
```

### Download playlist

For this you will have to configure a YouTube API key

#### Get API key

1. Go to the [Developer console dashboard](https://console.cloud.google.com/home/dashboard) and click on _CREATE PROJECT_, you can name the project and then press _CREATE_
1. Now go to the [Credentials tab](https://console.cloud.google.com/apis/credentials) and click on _CREATE CREDENTIALS_ and choose _API key_, copy the API key you see and save it somewhere safe, then you can click on _CLOSE_
1. Now go to the [YouTube API tab](https://console.cloud.google.com/apis/api/youtube.googleapis.com) and click on _ENABLE_

#### In Python

```py
from yt2mp4 import download_playlist
download_playlist(id, api_key)
'''
 - the first argument is the id of the playlist, you can pass either of the following forms
                    - https://www.youtube.com/watch?v=***********&list=PLAYLIST_ID
                    - https://www.youtube.com/playlist?list=PLAYLIST_ID
                    - PLAYLIST_ID
 - the second argument is the API key
 - the third is the extension, the default value is 'mp4'
 - the fourth one is the fps, the default value is 60
 - the last one is the binary path to the geckodriver
'''
```

#### In cmd

```sh
# each of those will convert to other formats
ytp2mp4
ytp2webm
ytp2mkv
ytp2flv
ytp2wmv
ytp2avi
ytp2mov
ytp2m4v
ytp2mp3
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
