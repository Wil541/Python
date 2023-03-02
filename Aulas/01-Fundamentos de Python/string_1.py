nome = "Willian"

print(nome.upper())     # Tudo MAIÚSCULA
print(nome.lower())     # Tudo MINÚSCULO
print(nome.title())     # Primeiro em Maiúsculo

texto = "  Olá, Mundo!    "     # texto com espaços em branco

print(texto + ".")
print(texto.strip()+ ".")
print(texto.rstrip()+ ".")
print(texto.lstrip()+ ".")

menu = "Python"

print(("####" + menu + "####"))
print(menu.center(14, "#"))         # Junçoes e centralização
print("P-y-t-h-o-n")
print("-".join(menu))               # interação

for letra in menu:
    print(letra, end="-")           # neste caso iria colocar ate o fim iria ser necessário controlar o for para evitar este caso. Muito mais fácil fazer com a função .join
print()