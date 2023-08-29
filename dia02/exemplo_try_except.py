#Refazendo o exemplo do dia anterior utilizando também Try e Except

num = input("Digite um Número: ")

antecessor = 0
sucessor = 0

try:
    antecessor = int(num)-1
    sucessor = int(num)+1
except ValueError:
    raise ValueError("Digite um número Válido")

print(f" O número é {num}, Seu Antecessor é :{antecessor} e Seu Sucessor é :{sucessor}.")