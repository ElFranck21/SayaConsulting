# models/maquiladores.py
from .db import get_connection

mydb = get_connection()

class Maquilador:
    def __init__(self, ape_mat='', ape_pat='', direction='', id_maquilador='', name=''):
        self.ape_mat = ape_mat
        self.ape_pat = ape_pat
        self.direction = direction
        self.id_maquilador = id_maquilador
        self.name = name

    @staticmethod
    def get_all():
        maquiladores = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM maquiladores"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                maquilador = Maquilador(ape_mat=row["ape_mat"],
                                        ape_pat=row["ape_pat"],
                                        direction=row["direction"],
                                        id_maquilador=row["id_maquilador"],
                                        name=row["name"])
                maquiladores.append(maquilador)
        return maquiladores
