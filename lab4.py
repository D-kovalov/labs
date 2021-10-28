import requests
from requests.structures import CaseInsensitiveDict
import sqlite3
url = "http://api.weatherstack.com/current?access_key=eba7879de5317e16bdfef8d7498b4d63&query=Kharkiv%20"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "@dVFDHfilename"


#resp = requests.post(url, headers=headers, data=data)
resp1=requests.get(url)
print(resp1.content)
try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite\n")

    cursor.execute("""DROP TABLE requests""")

    cursor.execute("""CREATE TABLE IF NOT EXISTS requests(
        response TEXT);
        """)

    sqlite_insert_with_param = """INSERT INTO requests
                              (response)
                              VALUES (?);"""

    data_tuple = (resp1.text,)
    cursor.execute(sqlite_insert_with_param, data_tuple)

    sqlite_insert_with_param = """INSERT INTO requests
                              (response)
                              VALUES (?);"""




    cursor.execute(sqlite_insert_with_param, data_tuple)

    cursor.execute("SELECT * FROM requests;")
    result = cursor.fetchmany(999)
    print(result)

    sqlite_connection.commit()
    print("\nЗапись успешно вставлена в таблицу requests ")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)
finally:
    if sqlite_connection:
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
