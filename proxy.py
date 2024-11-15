#Esse é o arquivo "proxy", responsável por cumprir a função do padrão de projeto Proxy. Essa classe está controlando o meu acesso com o Banco de Dados, garantindo a segurança e estabilidade da minha aplicação. Ela está auxiliando na estrutura do projeto pois deixa a conexão com o Banco de Dados mais fácil de se realizar, apenas chamando essa classe sempre que precisar dessa conexão.
from database import createConnection

class DatabaseProxy:
    def __init__(self):
        self._connection = None

    def getConnection(self):
        if not self._connection:
            self._connection = createConnection()
        return self._connection

    def closeConnection(self):
        if self._connection and self._connection.is_connected:
            self._connection.close()
            self._connection = None
            print("Conexão ao banco de dados fechada")