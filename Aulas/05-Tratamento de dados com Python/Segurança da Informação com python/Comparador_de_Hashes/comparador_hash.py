    # HASH
    # O Hash é como se fosse um identificador único de um algoritmo que vai analisar vyte a byte de determinado dado para gerar de forma única, jum determinado código que só aquele arquivo terá. Se neste mesmo arquivo um único bit for alterado o hash gerado será diferente
    # site para decodificar hash: https://md5decrypt.net.en/


import hashlib

arquivo1 ="Arquivo_a.txt"
arquivo2 ="Arquivo_b.txt"


hash1 = hashlib.new("ripemd160")                # Informa o algoritmo de hash que irá ser utilizado (ripemd 160 bytes)
hash1.update(open(arquivo1, "rb").read())       # Quem irá fazer a comparação do hash (abriu o arquivo desejado para comparar, rb = modo de leitura no modo binário)

hash2 = hashlib.new("ripemd160")                # Informa o algoritmo de hash que irá ser utilizado (ripemd 160 bytes)
hash2.update(open(arquivo2, "rb").read())       # Quem irá fazer a comparação do hash (abriu o arquivo desejado para comparar, rb = modo de leitura no modo binário)

if hash1.digest()!= hash2.digest():             # Irá comparar os arquivos e verificar se são diferentes e printar as hashs de cada um
    print(f"O arquivo: {arquivo1} é DIFERENTE do arquivo: {arquivo2}")
    print(f"O hash do {arquivo1} é: ", hash1.hexdigest())
    print(f"O hash do {arquivo2} é: ", hash2.hexdigest())

else:
    print(f"O arquivo: {arquivo1} é IGUAL do arquivo: {arquivo2}")
    print(f"O hash do {arquivo1} é: ", hash1.hexdigest())
    print(f"O hash do {arquivo2} é: ", hash2.hexdigest())