from sqlite3 import *


def init_data_base():
    """
    Данная функция должна вызываться один раз при первом запуске приложения она

    """
    cursor.execute("CREATE TABLE Users (Email TEXT, Age INTEGER, Height INTEGER, Weight INTEGER, Password INTEGER, Language TEXT);")
    cursor.execute("CREATE TABLE Values_Graph(Password INTEGER, X TEXT, Y REAL);")
    print("Successful creation of database")


con = connect(rf'../Screens/dataBase.sqLite')
cursor = con.cursor()

init_data_base()
cursor.close()
con.close()