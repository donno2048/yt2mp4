from setuptools import setup, find_packages
setup(
    name='yt2mp4',
    version='1.0.5',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description='Download YouTube videos and playlists as MP4 files (and other formats)',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/donno2048/yt2mp4',
    project_urls={
        'Documentation': 'https://github.com/donno2048/yt2mp4#readme',
        'Bug Reports': 'https://github.com/donno2048/yt2mp4/issues',
        'Source Code': 'https://github.com/donno2048/yt2mp4',
    },
    python_requires='>=3.0',
    packages=find_packages(),
    install_requires=['selenium>=4.1.0', 'selenium-wire>=4.5.6', 'moviepy>=1.0.3'],
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [
        'yt2mp4=yt2mp4.__main__:mp4',
        'yt2webm=yt2mp4.__main__:webm',
        'yt2mkv=yt2mp4.__main__:mkv',
        'yt2flv=yt2mp4.__main__:flv',
        'yt2wmv=yt2mp4.__main__:wmv',
        'yt2avi=yt2mp4.__main__:avi',
        'yt2movie=yt2mp4.__main__:mov',
        'yt2m4v=yt2mp4.__main__:m4v',
        'yt2mp3=yt2mp4.__main__:mp3',
        'ytp2mp4=yt2mp4.__main__:pmp4',
        'ytp2webm=yt2mp4.__main__:pwebm',
        'ytp2mkv=yt2mp4.__main__:pmkv',
        'ytp2flv=yt2mp4.__main__:pflv',
        'ytp2wmv=yt2mp4.__main__:pwmv',
        'ytp2avi=yt2mp4.__main__:pavi',
        'ytp2movie=yt2mp4.__main__:pmov',
        'ytp2m4v=yt2mp4.__main__:pm4v',
        'ytp2mp3=yt2mp4.__main__:pmp3'
    ] }
)
