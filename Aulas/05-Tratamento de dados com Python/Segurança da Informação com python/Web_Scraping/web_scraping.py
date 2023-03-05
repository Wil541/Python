    # Um web scraper é uma ferramenta de coleta de dados web, uma forma de mineração que permite a esxtração de dados de sites da web convertendo-os em informação estruturada para posterior análise

from bs4 import BeautifulSoup       # Importa biblioteca BeautifulSoup: permite extração de dados de arquivos HTML e XML
import requests                     # Importa biblioteca requests: permite que vocÊ envie solicitações HTTP em Python

site = requests.get("https://www.climatempo.com.br/").content       # Objeto site recebendo o conteúdo da requisição http do site

soup = BeautifulSoup(site, 'html.parser')                           # Objeto soup baixando do site o html

#print(soup.prettify())                                              # Transforma o html em string e printa

temperatura = soup.find("span", class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5") # Sempre colocar o underline apos class

print(temperatura.string)
print(soup.title.string)        # Imprime apenas as strings presente em título
print(soup.a)                   # Primeira tag que encontra como âncora
print(soup.a.string)            # Imprime apenas as strings presente em âncora
print(soup.p.string)            # Imprime apenas as strings presente em p
print(soup.find('admin'))       # Imprime informações encontradas sobre o administrador