import matplotlib.pyplot as plt
def urunler_satis_grafigi(df, output_dir):
    plt.figure(figsize = (10,6))
    plt.bar(df['product_name'], df['total_sales'])
    plt.title('Urun Bazlı Satışlar')
    plt.xlabel('Urunler')
    plt.ylabel('Toplam Satışlar')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig(output_dir /'urun_satislar_grafigi.png')
    plt.close()