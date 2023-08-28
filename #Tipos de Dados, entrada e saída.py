#Tipos de Dados, entrada e saída
#Criação de variáveis sem passar tipo

nome = "Gabriel"
idade = "20"
humano = False

#Criando variáveis passando o tipo de dado

nome: str = "Gabriel"
idade: int = 20
humano: bool = True

print(nome)

#TypeCasting

numero = "10" #numero é uma string

numero2 = int(numero) #Casting para inteiro (mudança de variável para inteiro)

#função type(x) retorna o tipo da variável "x"

#Output/Print
print("hello world")

#Entrada de informações/Input
num = input("num: ")

#pode-se utilizar o input direto em uma condicional (sem utilizar uma variável)

if int(input("num: ")) < 10:
    print("O número digitado é maior que 10")

