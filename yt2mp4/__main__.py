from . import download, download_playlist
def mp4(): download(input("https://www.youtube.com/watch?v="), outname='out.mp4')
def webm(): download(input("https://www.youtube.com/watch?v="), outname='out.webm')
def mkv(): download(input("https://www.youtube.com/watch?v="), outname='out.mkv')
def flv(): download(input("https://www.youtube.com/watch?v="), outname='out.flv')
def wmv(): download(input("https://www.youtube.com/watch?v="), outname='out.wmv')
def avi(): download(input("https://www.youtube.com/watch?v="), outname='out.avi')
def mov(): download(input("https://www.youtube.com/watch?v="), outname='out.mov')
def m4v(): download(input("https://www.youtube.com/watch?v="), outname='out.m4v')
def mp3(): download(input("https://www.youtube.com/watch?v="), outname='out.mp3')
def pmp4(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "mp4")
def pwebm(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "webm")
def pmkv(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "mkv")
def pflv(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "flv")
def pwmv(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "wmv")
def pavi(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "avi")
def pmov(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "mov")
def pm4v(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "m4v")
def pmp3(): download_playlist(input("https://www.youtube.com/playlist?list="), input("API key: "), "mp3")
if __name__ == '__main__': mp4()
