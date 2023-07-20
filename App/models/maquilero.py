# models/maquilero.py
from .db import get_connection

mydb = get_connection()

class Maquilero:
    def __init__(self, ape_mat='', ape_pat='', direction='', id_maquilero='', name=''):
        self.ape_mat = ape_mat
        self.ape_pat = ape_pat
        self.direction = direction
        self.id_maquilero = id_maquilero
        self.name = name

    @staticmethod
    def get_all():
        maquileros = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM maquilero"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                maquilero = Maquilero(ape_mat=row["ape_mat"],
                                      ape_pat=row["ape_pat"],
                                      direction=row["direction"],
                                      id_maquilero=row["id_maquilero"],
                                      name=row["name"])
                maquileros.append(maquilero)
        return maquileros
