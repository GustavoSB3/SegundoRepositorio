import mysql.connector

try:
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="gure2408",
        database="login"
    )

    cursor = conexao.cursor(dictionary=True)
    cursor.execute("SELECT * FROM usuarios;")

    for linha in cursor.fetchall():
        print(linha)

except mysql.connector.Error as err:
    print(f"Erro ao conectar ou consultar o banco: {err}")

finally:
    if conexao.is_connected():
        cursor.close()
        conexao.close()
        print("Conexão encerrada.")