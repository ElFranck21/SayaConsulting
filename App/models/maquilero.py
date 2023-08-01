# models/maquilero.py
from .db import get_connection

mydb = get_connection()

class Maquilero:
    def __init__(self, name='', ape_mat='', ape_pat='', direction='',id_maquilero=''):
        self.name = name
        self.ape_mat = ape_mat
        self.ape_pat = ape_pat
        self.direction = direction
        self.id_maquilero = id_maquilero
    def save(self):
        with mydb.cursor() as cursor:
            sql = "INSERT INTO maquilero (ape_mat, ape_pat, direction, name) VALUES (%s, %s, %s, %s)"
            values = (self.name, self.ape_mat, self.ape_pat, self.direction)
            cursor.execute(sql, values)
        mydb.commit()

    @staticmethod
    def get_all():
        maquilero = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM maquilero"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                maquilero = Maquilero(name=row["name"],
                                      ape_pat=row["ape_pat"],
                                      ape_mat=row["ape_mat"],
                                      direction=row["direction"],
                                      id_maquilero=row["id_maquilero"])
                maquilero.append(maquilero)
        return maquilero
