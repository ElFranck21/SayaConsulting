# models/supplier.py
from .db import get_connection

mydb = get_connection()

class Supplier:
    def __init__(self, ape_mat='', ape_pat='', direction='', id_material='', id_supplier='', name=''):
        self.ape_mat = ape_mat
        self.ape_pat = ape_pat
        self.direction = direction
        self.id_material = id_material
        self.id_supplier = id_supplier
        self.name = name

    @staticmethod
    def get_all():
        suppliers = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM supplier"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                supplier = Supplier(ape_mat=row["ape_mat"],
                                    ape_pat=row["ape_pat"],
                                    direction=row["direction"],
                                    id_material=row["id_material"],
                                    id_supplier=row["id_supplier"],
                                    name=row["name"])
                suppliers.append(supplier)
        return suppliers
