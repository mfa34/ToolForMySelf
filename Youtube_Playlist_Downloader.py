from pytube import Playlist

# YouTube oynatma listesinin URL'sini girin

playlist_url = "Youtube Playlist URL"


# Playlist nesnesi oluşturun
playlist = Playlist(playlist_url)

# Tüm videoları indirin
for video in playlist.videos:
    video.streams.get_highest_resolution().download(output_path="YourPath")
