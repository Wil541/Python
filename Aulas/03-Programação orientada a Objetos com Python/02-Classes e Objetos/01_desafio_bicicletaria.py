class Bicicleta:
    # inicializador com as caracteristicascuidado pois possui 2 underline antes e depois de "init" self é uma referencia ao objeto
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1

    def buzinar(self):          # os comportamentos são definidos pelos metodos e declarar o metodo obrigatoriamente dentro do argumento "self"
        print("Plin plim...")   # barulho sonoro da buzinha

    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada!")

    def correr(self):
        print("Vrummmmmm...")

    def trocador_marcha(self, nro_marcha):
        print("Trocando marcha")

        def _trocador_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else:
                print("não foi possivel trocar de marcha...")

    def get_cor(self):
        return self.cor

   # def __str__(self):
       # return f"Bicicleta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}"

    def __str__(self):
        # com essa representação é possivel inserir mais caracteristicas sem se preocupar pq quando chamado irá atualizar automaticamente apenas acrescentando em (def __init__)
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Verde", "Monark", 2000, 189)
print(b2)
Bicicleta.buzinar(b2)           # é necessário o argumento b2 == self
# é a mesma função acima porem não é necessario parrar o argunto dentro dos parenteses
b2.buzinar()
print(b2.get_cor())
print(b2.cor)                   # é a mesma função acima porém é mais usual
