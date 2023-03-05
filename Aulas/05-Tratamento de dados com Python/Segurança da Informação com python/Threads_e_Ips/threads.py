import time
from threading import Thread

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        trajeto += velocidade
        time.sleep(0.5)
        print("Piloto: {} Km:{} \n" .format(piloto, trajeto))


t_carr01 = Thread(target=carro, args=[1, "Bruno"])
t_carr02 = Thread(target=carro, args=[2, "Python"])

t_carr01.start()
t_carr02.start()