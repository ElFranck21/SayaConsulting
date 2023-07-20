# models/positions.py
from .db import get_connection

mydb = get_connection()

class Position:
    def __init__(self, id_position='', machinery_in_use='', name_position=''):
        self.id_position = id_position
        self.machinery_in_use = machinery_in_use
        self.name_position = name_position

    @staticmethod
    def get_all():
        positions = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM positions"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                position = Position(id_position=row["id_position"],
                                    machinery_in_use=row["machinery_in_use"],
                                    name_position=row["name_position"])
                positions.append(position)
        return positions
