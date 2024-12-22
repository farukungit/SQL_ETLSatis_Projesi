import matplotlib.pyplot as plt
def musteri_satis_grafigi(df, output_dir):
    plt.figure(figsize = (10,6))
    plt.bar(df['customer_name'], df['total_spent'])
    plt.title('En cok harcama yapan 5 müsteri')
    plt.xlabel('Müsteriler')
    plt.ylabel('Toplam Harcama Miktarı')
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.savefig(output_dir  /'musteri_satislar_grafigi.png')
    plt.close()