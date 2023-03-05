    # WEB CRAWLER
    # Web crawler é uma ferramenta usada para encontrar ler e indexar páginas de um site. É como um robô que captura informações de cada um dos links que encontra pela frente, cadastra e compreende o que é mais relevante. (palavras-chaves)
    # Muito utilizado em levantamento de informações em um processo de Pentest



import requests                     # É uma biblioteca que permite que você envie solicitações HTTP em Python
from bs4 import BeautifulSoup       # É uma biblioteca de extração de dados de arquivos HTML e XML
import operator                     # Exporta um conjunto de funções eficientes correspondentes aos operadores intríncecos do Python como: +-*/ not and
from collections import Counter     # Nos ajuda a preencher e manipular eficientemente as estruturas de dados como tuplas, dicionários e listas


def start(url):

    wordlist = []                                           # Ira armazenar o conteúdo do site informado
    source_code = requests.get(url).text

    soup = BeautifulSoup(source_code, 'html.parser')        # Requisição dos dados da url e tranforma em HTML

    # Text in given web-page is stored under
    # The <div> tags with class <entry-content>
    for each_text in soup.findAll('div', {'class': 'entry-countent'}):      # Vai procurar o conteúdo que houver com div e class no site e tranforma de HTML para texto
        content = each_text.text


        words = content.lower().split()             # Transforma o conteúdo em letras minúsculas, e faz o split (cada conteúdo sera uma linha)

        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)


def clean_wordlist(wordlist):                       # Retira os caracteres informados de wordlist
    clean_list = []                                 # Cria uma nova lista
    for word in wordlist:
        symbols = '!@#$%¨&*()_+={[}]|\;:"<>?/., '   # Retira os caracteres

        for i in range(0, len(symbols)):            # Caso encontrado um dos simbolos informados irasubstituir por nada ou seja apaga-lo
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):              # Cria um dicionário com as palavras
    word_count = {}                             # conta cada palavra

    for word in clean_list:                     # Conta a quantidade de vezes que a palavra foi utilizadas no site
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1




    for key, value in sorted(word_count.items(),
                             key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)


    top =  c.most_common(10)        # Top 10 palavras mais utilizadas no site
    print(top)                      # Exibe as 10 palavras mais utilizadas



if __name__ == '__main__':
    start("https://www.geeksforgeeks.org/python-programming-language/?ref=leftbar")