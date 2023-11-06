from pytube import Playlist

# YouTube oynatma listesinin URL'sini girin
playlist_url = "https://www.youtube.com/playlist?list=PLBn2Il2MsKWR4VitZgzWtVfuqnMjTIs-F"

# Playlist nesnesi oluşturun
playlist = Playlist(playlist_url)

# Tüm videoları indirin
for video in playlist.videos:
    video.streams.get_highest_resolution().download(output_path="C:/Users/salih/Music/Telefon/NasihatlarPlaylist")
