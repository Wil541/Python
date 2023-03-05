import phonenumbers     # Fornece vários recursos, como informações básicas de um número de telefone, validação de um numero de telefone, etc

from phonenumbers import geocoder

phone = input('Digite o telefone no formato +551140028922: ')

phone_numbers = phonenumbers.parse(phone)

print("Este telefone é da região da/de ou da/do: " + geocoder.description_for_number(phone_numbers, 'pt'))