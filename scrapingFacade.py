#Esse é o arquivo "scrapingFacade" responsável pela funcionalidade do padrão de projeto Facade. Esse arquivo está ajudando muito na estrutração e na simplificação do projeto pois reune todas as principais funções utilizadas na hora de fazer o "scraping", assim eu consigo deixar o código mais simples e mais fácil de se entender, pois não preciso ficar chamando todas essas funções sempre que precisar, posso apenas acessar a função que eu preciso da classe que eu preciso em qualquer parte do projeto.
from database import addProduct
from scraper import fetchPage, getDiscountProducts
from proxy import DatabaseProxy
from adapter import ProductAdapter
from tabulate import tabulate

class ScrapingFacade:
    def __init__(self, dbProxy):
        self.dbProxy = dbProxy

    def scrapeAndStore(self, url):
        conn = self.dbProxy.getConnection()
        if not conn:
            print("Erro ao abrir a conexão com o banco de dados")
            return

        pageContent = fetchPage(url)
        if not pageContent:
            print("Erro ao buscar conteúdo da página")
            return

        discountedProducts = getDiscountProducts(pageContent)

        print("\nProdutos com desconto encontrados:")
        if discountedProducts:
            tableData = [[p['title'], p['price'], p['url']] for p in discountedProducts]
            headers = ["Título", "Preço", "URL"]
            print(tabulate(tableData, headers, tablefmt="grid"))
        else:
            print("Nenhum produto com desconto encontrado.")

        for product in discountedProducts:
            #Aqui eu estou usando o adapter pois a minha aplicação espera um Objeto como retorno, porém ele recebe um array, então uso o Adapter para converter esse tipo de dado.
            adaptedProduct = ProductAdapter.adapt(product)
            addProduct(conn, adaptedProduct['title'], adaptedProduct['url'], adaptedProduct['price'])
        
        self.dbProxy.closeConnection()
        