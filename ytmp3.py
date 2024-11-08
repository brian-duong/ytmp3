from pathlib import Path
from pytubefix import YouTube 
import os

links = '\links.txt'
linkPath = str(Path.cwd()) + links
contents = Path(linkPath).read_text()
toDownload = contents.split('\n')
for url in toDownload:
    yt = YouTube(url)
    print(f"Downloading \"{yt.title}\"")
    video = yt.streams.filter(only_audio=True).first()
    destination = str(Path.cwd()) + '\MP3s'
    outFile = video.download(output_path=destination)
    base, ext = os.path.splitext(outFile)
    newFile = base + '.mp3'
    os.rename(outFile, newFile)