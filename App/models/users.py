# models/users.py
from .db import get_connection
from werkzeug.security import generate_password_hash, check_password_hash

mydb = get_connection()

class User:
    def __init__(self, username='', email='', password='', ape_mat='', ape_pat='', direction='', name='', image='', id_position='', id_role='', id_user=''):
        self.username = username
        self.email = email
        self.password = password
        self.ape_mat = ape_mat
        self.ape_pat = ape_pat
        self.direction = direction
        self.name = name
        self.image = image
        self.id_position = id_position
        self.id_role = id_role
        self.id_user = id_user
    
    def save(self):
        with mydb.cursor() as cursor:
            self.password = generate_password_hash(self.password)
            sql = "INSERT INTO users (name, email, password, ape_mat, ape_pat, direction, username, id_position, id_role) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            values = (self.name, self.email, self.password, self.ape_mat, self.ape_pat, self.direction, self.username, self.id_position, self.id_role)
            cursor.execute(sql, values)
        mydb.commit() 
    
    @staticmethod
    def get_all():
        users = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                user = User(ape_mat=row["ape_mat"],
                            ape_pat=row["ape_pat"],
                            direction=row["direction"],
                            email=row["email"],
                            id_position=row["id_position"],
                            id_role=row["id_role"],
                            id_user=row["id_user"],
                            image=row["image"],
                            name=row["name"],
                            password=row["password"],
                            username=row["username"])
                users.append(user)
        return users

    @staticmethod
    def check_username(username):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_user FROM users WHERE username = %s"
            cursor.execute(sql, (username,))
            result = cursor.fetchone()
            return result is not None

    @staticmethod
    def check_email(email):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT id_user FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
            result = cursor.fetchone()
            return result is not None

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Position:
    def __init__(self, id_position='', name_position=''):
        self.id_position = id_position
        self.name_position = name_position
    
    @staticmethod
    def get_all():
        positions = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM positions"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                position = Position(id_position=row["id_position"], name_position=row["name_position"])
                positions.append(position)
        return positions


class Role:
    def __init__(self, id_role='', name_role=''):
        self.id_role = id_role
        self.name_role = name_role
    
    @staticmethod
    def get_all():
        roles = []
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM roles"
            cursor.execute(sql)
            result = cursor.fetchall()
            for row in result:
                role = Role(id_role=row["id_role"], name_role=row["name_role"])
                roles.append(role)
        return roles

    @staticmethod
    def get_by_password(email, password):
        with mydb.cursor(dictionary=True) as cursor:
            sql = "SELECT * FROM users WHERE email = %s"
            cursor.execute(sql, (email,))
            user_data = cursor.fetchone()

            if user_data and check_password_hash(user_data["password"], password):
                return User(**user_data)
            else:
                return None