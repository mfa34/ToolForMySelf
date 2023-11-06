from pytube import Playlist

# YouTube oynatma listesinin URL'sini girin
<<<<<<< HEAD
playlist_url = "https://www.youtube.com/playlist?list=PLBn2Il2MsKWR4VitZgzWtVfuqnMjTIs-F"
=======
playlist_url = "Youtube Playlist URL"
>>>>>>> bbd2c02c34d375676ab05c14b796f8669cabe8f3

# Playlist nesnesi oluşturun
playlist = Playlist(playlist_url)

# Tüm videoları indirin
for video in playlist.videos:
<<<<<<< HEAD
    video.streams.get_highest_resolution().download(output_path="C:/Users/salih/Music/Telefon/NasihatlarPlaylist")
=======
    video.streams.get_highest_resolution().download(output_path="YourPath")
>>>>>>> bbd2c02c34d375676ab05c14b796f8669cabe8f3
