from pytube import YouTube

url = "https://www.youtube.com/watch?v=WRyzVaf46Ts&t=1010s"

video_youtube = YouTube(url)

print("Nom video : "+ video_youtube.title)