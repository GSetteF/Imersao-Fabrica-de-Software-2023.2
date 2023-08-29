#Exercicio: Crie um programa que va de 0 à 30, mas pare quando encontrar o 20

counter = 0

while counter <= 30:
    if counter == 20:
        print("Chegou no 20.")
        break

    print(counter)
    counter+=1
