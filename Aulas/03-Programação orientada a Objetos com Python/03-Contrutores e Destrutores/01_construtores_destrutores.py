class Cachorro:
    def __init__(self, nome, cor, acordado = True):         # Contrutor, criado no inicio
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):                                      # Destrutor, criado no final quando o objeto for destruido
        print("Removendo a instância da classe")
    
    def falar(self):
        print("AuAu")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco e preto", False)
    print(c.nome)

c = Cachorro("Chappie", "Amarelo")
c.falar()

criar_cachorro()