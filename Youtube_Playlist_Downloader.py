from pytube import Playlist

# YouTube oynatma listesinin URL'sini girin
playlist_url = "https://www.youtube.com/playlist?list=PL6QeoSH9jbAYdNSD2AugNL0zvcAqvJiUl"

# Playlist nesnesi oluşturun
playlist = Playlist(playlist_url)

# Tüm videoları indirin
for video in playlist.videos:
    video.streams.get_highest_resolution().download(output_path="D:/AILE/FATIH/Kuran-i_Kerim_Tefsir_Dersleri_Orhan_Karmis_Hoca")
