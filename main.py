from pytube import YouTube
import sys


# Path where the file will be saved
path = "E:\Download\youtube_downloads"
link = sys.argv[1]  # Getting the link from the command prompt


def on_progress(vid, chunk, bytes_remaining):
    '''To display the progress bar and the details.'''
    current = ((vid.filesize - bytes_remaining)/vid.filesize)
    progress = int(50*current)
    status = '█' * progress + '-' * (50 - progress)
    total_size = vid.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    totalsz = (total_size/1024)/1024
    totalsz = round(totalsz, 1)
    remain = (bytes_remaining / 1024) / 1024
    remain = round(remain, 1)
    dwnd = (bytes_downloaded / 1024) / 1024
    dwnd = round(dwnd, 1)
    percentage_of_completion = round(percentage_of_completion, 1)
    sys.stdout.write(
        f'↳ |{status}| {percentage_of_completion}% \nDownload Progress: {percentage_of_completion}%, Total Size:{totalsz} MB, Downloaded: {dwnd} MB, Remaining:{remain} MB\n\n')
    sys.stdout.flush()


def complete(stream, path):
    '''To display the message after completion of download'''
    print("\n\nDownload completed!")


yt = YouTube(link, on_progress_callback=on_progress,
             on_complete_callback=complete)
print("Title: ", yt.title)
print("Download has started.")

yt = yt.streams.get_by_itag(137)  # Getting the video of resolution 1080p.

yt.download(path)
