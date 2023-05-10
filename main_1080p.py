from pytube import YouTube
import moviepy.editor as mpe
import sys
import os


# Path where the file will be saved
path = "E:\Download\youtube_downloads"
link = sys.argv[1]  # Getting the link from the command prompt

# For merging audio and video
vname = f"{path}\clip.mp4"
aname = f"{path}/audio.mp3"


def on_progress(vid, chunk, bytes_remaining):
    '''To display the progress bar and the details.'''
    current = ((vid.filesize - bytes_remaining)/vid.filesize)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion, 1)
    sys.stdout.write(
        f'↳ |{status}| {percentage_of_completion}% Down: {dwnd} MB Rem:{remain} MB\r')
    sys.stdout.flush()


def complete(stream, path):
    '''To display the message after completion of download'''
    print("\n\nFile download completed!")


# To download the video
yt_video = YouTube(link, on_progress_callback=on_progress,
                   on_complete_callback=complete)
vid_name = yt_video.title
print("Title: ", vid_name)
print("Downloading video file....")

# Getting the video of resolution 1080p.
yt_video = yt_video.streams.filter(
    subtype='mp4', res="1080p").first().download(path)
os.rename(yt_video, vname)

# To download the audio
print("Downloading audio file....")
yt_audio = YouTube(link, on_progress_callback=on_progress,
                   on_complete_callback=complete).streams.filter(only_audio=True).first().download(path)
os.rename(yt_audio, aname)

# Setting the audio to the video
yt_video = mpe.VideoFileClip(vname)
yt_audio = mpe.AudioFileClip(aname)
final = yt_video.set_audio(yt_audio)

# Output result
final.write_videofile(f"{path}\{vid_name}.mp4")
print("Video is ready to play!")

# To delete the seperate audio and video file
os.remove(vname)
os.remove(aname)
