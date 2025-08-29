import mysql.connector

conexao = mysql.connector.connect(
    host="127.0.0.1",
    port="3306",
    user="root",
    password="gure2408",
    database="login"

)

cursor = conexao.cursor()
cursor.execute("SELECT * FROM usuarios;")
for linha in cursor.fetchall():
    print(linha)

conexao.close()