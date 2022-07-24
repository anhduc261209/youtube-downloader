import requests
from pytube import YouTube
from youtube_dl import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

def search(arg):
	with YoutubeDL(YDL_OPTIONS) as ydl:
		try:
			requests.get(arg) 
		except:
			video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
		else:
			video = ydl.extract_info(arg, download=False)

	return video

def download(query, file_name, audio = False):
	url = YouTube(search(query)['webpage_url'])
	print("Start downloading...")
	if audio:
		video = url.streams.filter(only_audio = True, file_extension = "webm").first()
		video.download(filename = file_name + ".webm")
	else:
		video = url.streams.filter(progressive = True, file_extension='mp4').first()
		video.download(filename = file_name + ".mp4")
	print("Downloaded")

def get_input():
	query = input("Please type the link or query: ")
	file_name = input("Please input the file name (without extension): ")
	audio = input("Do you want audio (y/n)? ")
	if audio.lower() == "y": audio = True
	else: audio = False
	download(query, file_name, audio)

if __name__ == "__main__":
	get_input()