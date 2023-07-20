# models/type_of_material.py
from .db import get_connection

mydb = get_connection()

class TypeOfMaterial:
    def __init__(self, id_material='', name_material='', price=''):
        self.id_material = id_material
        self.name_material = name_material
        self.price = price

    @staticmethod
    def get_all():
        types_of_material = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM type_of_material"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                type_of_material = TypeOfMaterial(id_material=row["id_material"],
                                                  name_material=row["name_material"],
                                                  price=row["price"])
                types_of_material.append(type_of_material)
        return types_of_material
