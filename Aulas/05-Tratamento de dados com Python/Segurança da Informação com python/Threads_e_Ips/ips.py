import ipaddress        # Biblioteca que possibilita fazer calculo com IP,imprimir,  scanear, verificar entre outros

ip = '192.168.0.0/32'

rede = ipaddress.ip_network(ip, strict=False)       #Mesmo sendo falso irá exibir o IP

for ip in rede:
    print(ip)