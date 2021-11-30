from seleniumwire.webdriver import Firefox
from selenium.webdriver.firefox.webdriver import Options
from moviepy.editor import VideoFileClip, AudioFileClip
firefox_options = Options()
firefox_options.headless = True
def download(id, outname='output.mp4', fps=60):
    driver = Firefox(options=firefox_options) # needed
    driver.get('https://www.youtube.com/watch?v=%s' % id.replace('https://', '').replace('www.youtube.com/watch?v=', '').replace('youtu.be/', ''))
    vid, aud = list(map(lambda url: '&'.join(filter(lambda element: 'range' not in element, url.split('&'))), filter(lambda req: '---' in req and 'generate' not in req, map(lambda req: req.url, driver.requests))))[:2]
    VideoFileClip(vid).set_audio(AudioFileClip(aud)).write_videofile(outname,fps=fps)
    driver.quit()
