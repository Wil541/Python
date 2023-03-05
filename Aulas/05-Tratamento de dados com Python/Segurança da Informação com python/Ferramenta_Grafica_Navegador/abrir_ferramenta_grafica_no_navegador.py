import webbrowser       # Fornece uma interface de alto nível para permitir a exibição de documentos Web aos usuários
from tkinter import *   # Fornece interface padrão do Python para o kit de ferramentas gráficas Tk

root = Tk ( )                   # root ira representar o tkinter e não ha nome no sistema por isso o espaço vazio
root.title('Abrir Browser')     # Título da imagem/janela
root.geometry('300x200')        # Tamanho da imagem/janela

def google():
    webbrowser.open('www.google.com')   # url que irá ser aberta

mygoogle = Button(root, text = 'Abrir o Google', command=google).pack(pady=20)  # Insere um botão dentro da imagem criada
root.mainloop()