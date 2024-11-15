#Aqui é criado a classe ProductAdapter, que executa a função do padrão de projeto Adapter utilizado no projeto. Essa classe é responsável por converter o tipo de dado de Array para um Objeto, pois os dados que chegam para o Adapter normalmente vem como Array, porém toda a aplicação utiliza como Objeto. Essa classe está sendo muito útil pois facilita e simplifica o código na hora de fazer essa manutenção, pois não preciso repetir esse código por todo o meu projeto.
class ProductAdapter:
    @staticmethod
    def adapt(productData):
        adaptedProduct = {
            'title': productData['title'],
            'url': productData['url'],
            'price': float(productData['price'])
        }
        return adaptedProduct
    