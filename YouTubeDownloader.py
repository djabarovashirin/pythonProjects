### This Python script uses the pytube library to download a YouTube video given its URL.

from pytube import YouTube

try:
    url = input("Enter the YouTube URL: ")

    yt = YouTube(url)

    print("Title:", yt.title)
    print("Views:", yt.views)

    # Get the highest resolution stream
    yd = yt.streams.get_highest_resolution()

    # Download the video to the current directory
    yd.download('/Users/shirindjabarova/Downloads/DownloadedVideos')

    print('Download complete.')
except Exception as e:
    print('An error occurred:', str(e))