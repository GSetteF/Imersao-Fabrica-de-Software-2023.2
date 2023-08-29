#Exercicio2: Crie um programa que leia a velocidade de um carro e multe se passar com velocidade maior que 80 km/h. mostre que ele foi multado. a multa é de R$7 por cada km acima do limite.

vel = input("Insira sua velocidade em km/h: ") #receber velocidade

try:
    vel_int = int(vel)
    if vel_int > 80:                     #verificar se é passivel de multa + aplicar caso seja
        multa = 7*(vel_int-80)
        print(f"Você foi multado e o valor a pagar é R${multa}.")
    elif vel_int == 80:
        print("Atingindo velocidade limite.")
    else:
        print("Velocidade abaixo do limite.")

except ValueError:
    raise ValueError("Insira uma velocidade válida.")