from pytube import YouTube

"""
    streaming all the formats available for download
"""
link = input("Enter Video URL: ")
yt = YouTube(link)
videos = yt.streams.all()

video = list(enumerate(videos))

for i in video:
    print(i)

print("Select download format: ")
dn_option = int(input("Enter the number: "))

try:
    dn_video = videos[dn_option]
    fn = input('Save As: ')
    save_path = input("Enter path to save file: ")
    dn_video.download(save_path, filename=fn)
except:
    print("Error occurred")

print("Download Successful!!")
