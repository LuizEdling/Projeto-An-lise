import mysql.connector
from mysql.connector import Error
from config import DB_CONFIG

def createConnection():
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG['host'],
            user=DB_CONFIG['user'],
            password=DB_CONFIG['password'],
            database=DB_CONFIG['database']
        )

        if connection.is_connected():
            print("Conectado ao MySQL Server")
            return connection
        
    except Error as erro:
        print(f"Erro ao conectar ao MySQL: {erro}")
        return None

    connection.commit()

def addProduct(connection, produto, url, valor):
    cursor = connection.cursor()
    cursor.execute('''
        INSERT INTO produto (produto, url, valor)
        VALUES (%s, %s, %s)
    ''', (produto, url, valor))

    connection.commit()

def fetchAllProducts(connection):
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM produto')
    products = cursor.fetchall()

    return products