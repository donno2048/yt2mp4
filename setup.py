from setuptools import setup, find_packages
setup(
    name='yt2mp4',
    version='1.0.0',
    license='MIT',
    author='Elisha Hollander',
    author_email='just4now666666@gmail.com',
    description='Download YouTube videos as MP4 files',
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
    install_requires=['selenium==4.1.0', 'selenium-wire==4.5.6', 'moviepy==1.0.3'],
    classifiers=['Programming Language :: Python :: 3'],
    entry_points={ 'console_scripts': [ 'yt2mp4=yt2mp4.__main__:main' ] }
)
