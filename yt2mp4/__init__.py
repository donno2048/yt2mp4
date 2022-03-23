from json import loads
from urllib.request import urlopen
from seleniumwire.webdriver import Firefox
from selenium.webdriver.firefox.webdriver import Options
from moviepy.editor import VideoFileClip, AudioFileClip
firefox_options = Options()
firefox_options.headless = True
def download(id, outname='output.mp4', fps=60, binary_path=None):
    if binary_path: firefox_options.binary_location = binary_path
    driver = Firefox(options=firefox_options) # needed
    driver.get('https://www.youtube.com/watch?v=%s' % id.replace('https://', '').replace('www.', '').replace('music.', '').replace('youtube.com/watch?v=', '').replace('youtu.be/', ''))
    vid, aud = list(map(lambda url: '&'.join(filter(lambda element: 'range' not in element, url.split('&'))), filter(lambda req: '---' in req and 'generate' not in req, map(lambda req: req.url, driver.requests))))[:2]
    driver.quit()
    if outname.endswith('.mp4'):
        VideoFileClip(vid).set_audio(AudioFileClip(aud)).write_videofile(outname,fps=fps)
    elif outname.endswith('.webm'):
        VideoFileClip(vid).set_audio(AudioFileClip(aud)).write_videofile(outname,fps=fps,codec='libvpx-vp9')
    elif outname.endswith('.mkv'):
        VideoFileClip(vid).set_audio(AudioFileClip(aud)).write_videofile(outname,fps=fps,codec='libx264')
    elif outname.endswith('.flv'):
        VideoFileClip(vid).set_audio(AudioFileClip(aud)).write_videofile(outname,fps=fps,codec='flv')
    elif outname.endswith('.wmv'):
        VideoFileClip(vid).set_audio(AudioFileClip(aud)).write_videofile(outname,fps=fps,codec='wmv2')
    elif outname.endswith('.avi') or outname.endswith('.mov') or outname.endswith('.m4v'):
        VideoFileClip(vid).set_audio(AudioFileClip(aud)).write_videofile(outname,fps=fps,codec='mpeg4')
    elif outname.endswith('.mp3'):
        AudioFileClip(aud).write_audiofile(outname)
    else:
        raise Exception('Unknown file extension')
def download_playlist(id, api_key, extension='mp4', fps=60, binary_path=None):
    for video, name in map(lambda data: (data["snippet"]["resourceId"]["videoId"], data["snippet"]["title"]), loads(urlopen("https://www.googleapis.com/youtube/v3/playlistItems?playlistId=%s&part=snippet&maxResults=50&key=%s" % (id[id.find("list=") + 5 if id.find("list=") > 0 else 0:], api_key)).read())["items"]): download(video, name + "." + extension, fps=fps, binary_path=binary_path)
