# models/product.py
from .db import get_connection

mydb = get_connection()

class Product:
    def __init__(self, id_material='', id_product='', name_product='', price='', size=''):
        self.id_material = id_material
        self.id_product = id_product
        self.name_product = name_product
        self.price = price
        self.size = size

    @staticmethod
    def get_all():
        products = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM product"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                product = Product(id_material=row["id_material"],
                                  id_product=row["id_product"],
                                  name_product=row["name_product"],
                                  price=row["price"],
                                  size=row["size"])
                products.append(product)
        return products
