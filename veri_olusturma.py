import random
import datetime

class DataGenerator:
    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date

    def generate_sales_data(self, customers, products, num_records):
        sales_data = []
        for _ in range(num_records):
            sale_date = self.start_date + datetime.timedelta(days=random.randint(0, (self.end_date - self.start_date).days))
            customer_id = random.randint(1, len(customers))
            product_id = random.randint(1, len(products))
            quantity = random.randint(1, 10)
            unit_price = products[product_id - 1][1]
            total_price = quantity * unit_price
            sales_data.append((sale_date, customer_id, product_id, quantity, unit_price, total_price))
        return sales_data