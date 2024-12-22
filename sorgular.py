import pandas as pd

# Ay bazında satış toplamlarını getiren bir fonksiyon oluşturalım

def fetch_sales_by_month(connection):
    # SQL Sorgusu: Satışları ay bazlı gruplar ve toplam fiyatları hesaplar
    sorgu =  ''' SELECT strftime('%Y-%m', sale_date) AS month,
                    SUM(total_price) AS total_sales
                FROM sales
                GROUP BY month
    '''
    # Sorguyu çalıştıralım ve sonucu bir pandas DataFrame'e dönüştürelim
    return pd.read_sql_query(sorgu,connection)

# Ürün bazında satış miktarlarını ve toplam satışları getiren bir fonksiyon yazalım
def fetch_sales_by_product(connection):
    # SQL sorgusu ürün isimlerine göre satış miktarlarını ve toplam fiyatını hesaplayın
    sorgu = '''
            SELECT p.product_name,
                SUM(s.quantity) AS total_quantity,
                SUM(s.total_price) AS total_sales
            FROM sales s
            JOIN products p
            ON s.product_id = p.product_id
            GROUP BY p.product_name

'''
    return pd.read_sql_query(sorgu, connection)

# En çok harcama yapan ilk 5 müşteriyi getiren fonksiyon oluşturan
def fetch_top_customers(connection):
    # SQL Sorgusu: Müşterilerin isimlerine göre toplam harcamaları hesaplar ve en çok harcama yapanları sıralar.
    sorgu = '''
            SELECT c.first_name || ' ' || c.last_name AS customer_name,
                SUM(s.total_price) AS total_spent
            FROM sales s
            JOIN customers c
            ON s.customer_id = c.customer_id
            GROUP BY customer_name
            ORDER BY total_spent DESC
            LIMIT 5            
    '''
    return pd.read_sql_query(sorgu, connection)
