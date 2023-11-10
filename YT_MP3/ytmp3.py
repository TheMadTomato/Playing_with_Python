import yt_dlp
import os


def download_audio(link):
    # Download youtube audio with the yt_dlp module and save it as .opus. (NOTE: it only works on linux)
    with yt_dlp.YoutubeDL({'extract_audio': True, 'format': 'bestaudio', 'outtmpl': '%(title)s.opus'}) as video:
        info_dict = video.extract_info(link, download=True)
        video_title = info_dict['title']
        print(video_title)
        video.download(link)
        print("Successfully Downloaded")
        # move the downloaded file to the music folder
        os.system("mv *.opus ~/Music")


link = input("Enter Youtube Link: ")
download_audio(link)
