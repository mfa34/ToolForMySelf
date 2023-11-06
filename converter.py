import os
from moviepy.editor import *

# Dönüştürmek istediğiniz klasörün yolu
klasor_yolu = "C:/Users/salih/Music/Telefon/NasihatlarPlaylist"

# Klasördeki tüm dosyaları alın
dosya_listesi = os.listdir(klasor_yolu)

# Klasördeki sadece video dosyalarını seçin
video_dosyalari = [dosya for dosya in dosya_listesi if dosya.lower().endswith((".mp4", ".mkv", ".avi"))]

for video_dosyasi in video_dosyalari:
    video_path = os.path.join(klasor_yolu, video_dosyasi)

    # Video dosyasını yükleyin
    video = VideoFileClip(video_path)

    # MP3 dosyasının adını oluşturun
    mp3_dosyasi = os.path.splitext(video_dosyasi)[0] + ".mp3"
    mp3_path = os.path.join(klasor_yolu, mp3_dosyasi)

    # Video dosyasını MP3 olarak kaydedin
    video.audio.write_audiofile(mp3_path)

    # Belleği temizleyin
    video.close()

print(f"Tüm videolar MP3 dosyalarına dönüştürüldü ve {klasor_yolu} klasörüne kaydedildi.")
