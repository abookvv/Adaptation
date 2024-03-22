
from sqlite3 import *


con = connect(rf'dataBase.sqLite')
cursor = con.cursor()




class User():
    current_user = 0
    con = connect('dataBase.sqLite')
    cursor = con.cursor()

    def __init__(self, email=0, password=0, age=0, weight=0, height=0, language="RUS"):
        current_user = self
        self.age = age
        self.height = height
        self.weight = weight
        self.password = password
        self.email = email
        self.language = language

        self.graghic = Graghic()

    def create(self):
        cursor.execute(f"""
        INSERT INTO Users ( Email, Age, Height, Weight, Password, Language)
        VALUES ( "{self.email}", {self.age}, {self.height}, "{self.weight}", {self.password}, "{self.language}");
        """)
        con.commit()

    def updata_user_data(self):
        cursor.execute(f"""
            UPDATE "Users"
            SET "Email" = '{self.email}', "Age" = '{self.age}', "Height" = '{self.height}', "Weight" = '{self.weight}', "Password" = '{self.password}', "Language" =  '{self.language}'
            WHERE Password = '{self.password}';
            """)
        con.commit()

    def check_props(self):
        cursor.execute(
            f"""
            SELECT Email, Age, Height, Weight, Password, Language FROM Users
            WHERE Password = {self.password};
                """)
        res = cursor.fetchall()
        print(res)
        if len(res) != 0:
            self.email = res[0][0]
            self.age = res[0][1]
            self.height = res[0][2]
            self.weight = res[0][3]
            self.password = res[0][4]
            self.language = res[0][5]
            print(self.password)
            return True
        else:
            return False




class Graghic():
    def __init__(self):
        self.graph_val = {}

    def create_coords(self, password: int, x: str, y: int):
        if x in self.graph_val.keys():
            return False
        else:
            self.graph_val[x] = y
            cursor.execute(f"""
                INSERT INTO Values_Graph (Password, X, Y)
                VALUES ({password},  {x}, {y});
                """)
            print(password,  x, y)
            con.commit()
            return True

    def init_check_prop(self, password: int):
        cursor.execute(
            f"""
            SELECT X, Y FROM Values_Graph
            WHERE Password = {password};
                """)
        res = cursor.fetchall()
        self.graph_val = {}
        for i in res:
            self.graph_val[res[i][0]] = res[i][1]


user = User()

D = {
    'GoBack': {'ru': 'Вернуться', 'eng': 'Go back'},
    'Save': {'ru': 'Сохранить', 'eng': 'Save'}
}