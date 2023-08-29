#Exercicio: Crie um programa que receba uma idade e retorne se pode obter carteira de Motorista (CNH)

def verificar_idade(x): #função para verificar se o usuario pode ou nao receber a cnh
    if x >= 18:
        return True
    else:
        return False

idade = input("Insira uma idade: ") #recebimento da idade

try:                                 #verificação se o tipo de dado da idade é válido
    idade_int = int(idade)
    if verificar_idade(idade_int):
        print("Idade válida para se obter CNH.")
    else:
        print("Idade inválida para obter CNH.")

except ValueError:
    raise ValueError("Digite um valor de idade válido.")