class Animal:
    def __init__(self, nro_patas):
        self.nro_patas = nro_patas

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


class Mamifero(Animal):
    def __init__(self, cor_pelo, **kw):
        self.cor_pelo = cor_pelo
        super().__init__(**kw)


class Ave(Animal):
    def __init__(self, cor_bico, **kw):
        self.cor_bico = cor_bico
        super().__init__(**kw)

    def __str__(self):
        return 'ave 42'


# class Cachorro(Mamifero):
#    pass


class Gato(Mamifero):
    pass

# class Leao(Mamifero):
#    pass


class Ornitorrinco(Mamifero, Ave):
    def __init__(self, cor_bico, cor_pelo, nro_patas):
        self.cor_bico = cor_bico
        super().__init__(cor_pelo = cor_pelo, cor_bico = cor_bico, nro_patas = nro_patas)
        print (Ornitorrinco.__mro__)            # onde ira buscas as classes nas heranças


gato = Gato(nro_patas = 4, cor_pelo = "preto")
print(gato)

ornitorrinco = Ornitorrinco(
    nro_patas = 4, cor_pelo = "vermelho", cor_bico = "laranja")
print(ornitorrinco)
