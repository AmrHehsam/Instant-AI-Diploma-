from pytube import YouTube
from bs4 import BeautifulSoup
import requests

link = "https://www.youtube.com/watch?v=wIdYTHoTtw8"
SAVE_PATH = "E:\AI Diploma\Instant AI Diploma\Instant-AI-Diploma-\Session 10"

response = requests.get(link)
response.raise_for_status()

soup = BeautifulSoup(response.content, "html.parser")
video_title = soup.find("meta", property="og:title")["content"]
video_description = soup.find("meta", property="og:description")["content"]

print("Video Title:", video_title)
print("Video Description:", video_description)

yt = YouTube(link)
yt.streams.get_highest_resolution().download(output_path=SAVE_PATH)
print('Video Downloaded Successfully')
