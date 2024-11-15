from scrapingFacade import ScrapingFacade
from proxy import DatabaseProxy

#Percebe-se que com a utilização dos Padrões de Projeto o meu arquivo "main.py" ficou bem simplificado e fácil de ser entendido, economizando muitas linhas de código por meio do Facade e do Proxy.
if __name__ == "__main__":
    #Aqui é instanciada a classe DatabaseProxy, responsável por estabelecer e representar minha conexão com o Banco de Dados, eu utilizo ela pare que após o Scraping ele possa inserir os dados no Banco de Dados
    dbProxy = DatabaseProxy()
    #Aqui eu estou instanciando a minha classe ScrapingFacade, para acessar a função "scrapeAndStore" dessa classe, de maneira simplificada e otimizada.
    scrapingFacade = ScrapingFacade(dbProxy)

    url = "https://books.toscrape.com/"
    scrapingFacade.scrapeAndStore(url)