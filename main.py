# import pytube

# # set video url to download from youtube
# video_url = input("write your video URL:")

# # create a Youtube object
# yt = pytube.YouTube(video_url)

# # set video quality to download
# stream = yt.streams.get_highest_resolution()
# print("Video is being downloaded")

# # start download
# stream.download()

import yt_dlp

# Enter the URL for the download
url = input('Enter video URL:')

yt_opts = {
    'format': 'bestvideo/best',  # Downloads the best video and audio, combined
    'noplaylist': True,  # To avoid downloading playlists
}

with yt_dlp.YoutubeDL(yt_opts) as ydl:
    ydl.download([url])

print('video downloaded successfully.')