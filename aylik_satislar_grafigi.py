import matplotlib.pyplot as plt

def aylik_satis_grafigi_olusturma(df, outbup_dir):
    plt.figure(figsize=(10,6))
    plt.plot(df['month'], df['total_sales'],marker='o')
    plt.title('Aylik Satis Tutari')
    plt.xlabel('Aylar')
    plt.ylabel('Toplam Satis')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig(outbup_dir /'aylik_satis_grafik.png')
    plt.close()