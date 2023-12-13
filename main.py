import pytube

# set video url to download from youtube
video_url = input("write your video URL:")

# create a Youtube object
yt = pytube.YouTube(video_url)

# set video quality to download
stream = yt.streams.get_highest_resolution()
print("Video is being downloaded")

# start download
stream.download()
