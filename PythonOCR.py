from PIL import Image
import pytesseract
from docx import Document

# Başlangıç ve bitiş sayfalarını giriniz
start_page = 1
end_page = 128

# İşlem başladı uyarısı
print("İşlem başladı...")

# Klasördeki her resmin  işlenmesi
for page_number in range(start_page, end_page + 1):
    # Resmin adını oluşturun
    image_file = f'YourPath/٦- الايمان والإسلام_page-{page_number:04d}.jpg'

    # Word belgesi oluşturuluyor
    doc = Document()

    # Görüntüdeki metni tanıyor
    image = Image.open(image_file)
    text = pytesseract.image_to_string(image, lang='ara')  # Hintce icin = hin degerini kullaniniz.
    doc.add_paragraph(text)

    # DOCX belgesini kaydediyor
    output_file = f'YourFileName{page_number:04d}.docx'
    doc.save(output_file)

    print(f"Sayfa {page_number} tamamlandı. {output_file} dosyası oluşturuldu.")

# İşlem tamamlandı uyarısı
print("İşlem tamamlandı. Tüm sayfalar dönüştürüldü.")
