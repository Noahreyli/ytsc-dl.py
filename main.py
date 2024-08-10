import os
import time
import subprocess

from pytube import Playlist, YouTube

def run_playlist(pl):
    for video in pl:
        yt = YouTube(video)
        music = yt.streams.first()

        default_filename = music.default_filename.replace(' ', '-').replace('   ', '-').replace('(', '-').replace(')', '-')
        print("Downloading " + default_filename + "...")
        
        yt.streams.first().download(filename=default_filename)
        time.sleep(1)
        
        new_filename = default_filename[0:-3] + "mp3"
        print("### Converting to MP3 ###")
        
        ffmpeg = ('ffmpeg -i '+default_filename[0:-4] + "mp4.mp4"+' '+new_filename)
        subprocess.call(ffmpeg, shell=True)

    print("Download finished.")

def run_single(yt):
    music = yt.streams.first()
    default_filename = music.default_filename.replace(' ', '-').replace('   ', '-').replace('(', '-').replace(')', '-')
    print("Downloading " + default_filename + "...")
    yt.streams.first().download(filename=default_filename)
    time.sleep(1)
    new_filename = default_filename[0:-3] + "mp3"
    print("### Converting to MP3 ###")

    ffmpeg = ('ffmpeg -i ' + default_filename[0:-4] + 'mp4.mp4 ' + new_filename)
    print(ffmpeg)
    subprocess.call(ffmpeg, shell=True)

    print("Download finished.")

if __name__ == "__main__":
    options = input("[1] Youtube Playlist - [2] Youtube Single - [3] SoundCloud Playlist ou Single: ")
    if options == "1":
        url = input("Please enter the url of the playlist you wish to download: ")
        pl = Playlist(url)
        print('Number of videos in playlist: %s' % len(pl.video_urls))
        run_playlist(pl)
    elif options == "2":
        url = input("Please enter the url: ")
        yt = YouTube(url)
        run_single(yt)
    elif options == "3":
        url = input("Please enter the url SoundCloud: ")
        scdl = ('scdl -l '+url)
        subprocess.call(scdl, shell=True)
