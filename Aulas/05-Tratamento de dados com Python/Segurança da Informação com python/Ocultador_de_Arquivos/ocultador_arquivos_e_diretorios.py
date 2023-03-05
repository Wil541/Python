import ctypes           # Fornece tipos de dados compatíveis com C e permite funções de chamada em DLLs ou bibliotecas compartilhadas

pasta = input('Digite o caminho da pasta a ser ocultada \n'
              'Exemplo: (C:/pasta): ')
atributo_ocultar = 0x02

retorno = ctypes.windll.kernel32.SetFileAttributesW(pasta, atributo_ocultar)    # Permite que o arquivo seja manipulado e vire oculto atraves do atributo hexadecimal informado (0x02)

if retorno:
    print("Arquivo foi ocultado!")
else:
    print("Arquivo não foi ocultado!")