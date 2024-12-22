from fpdf import FPDF
from pathlib import Path

def create_pdf_report(output_dir):
    # PDF oluşturucu nesnesini başlat
    pdf = FPDF()
    
    # Yeni bir sayfa ekle
    pdf.add_page()

    # Başlık fontunu ayarla ve başlığı ekle
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(0, 10, 'Sales Report', 0, 1, 'C')  # 'Sales Report' başlığını ortala
    
    pdf.ln(10)  # Başlık ile grafikler arasına boşluk ekle

    # Eklenecek grafik dosyalarının listesini tanımla
    images = ['aylik_satis_grafik.png', 'urun_satislar_grafigi.png', 'musteri_satislar_grafigi.png']

    # Her bir grafik dosyasını PDF'e ekle
    for img in images:
        img_path = Path(output_dir) / img  # Grafik dosyasının tam yolunu oluştur
        pdf.image(str(img_path), x=10, y=None, w=190)  # Grafiği PDF'e ekle (genişliği 190 olarak ayarla)
        pdf.ln(10)  # Her grafik arasında boşluk bırak

    # Son olarak, PDF dosyasını belirlenen dizine kaydet
    pdf.output(str(output_dir / 'sales_report.pdf'))