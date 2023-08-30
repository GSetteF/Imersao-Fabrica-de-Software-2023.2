def soma(x: int|float,y: int|float) -> int | float: #definindo uma função, x e y são parâmetros
    """Soma x + y e retorna o resultado""" #Documentação (doc_string), verificar passando o mouse sobre a função
    return x + y

#a = soma(1,2) exemplo: a = 3

def print_subtracao(x: int|float, y: int|float) -> None:
    print(f"{x-y}")

def soma_sem_parametro() -> int | float:
    x = 5
    y = 5
    #print(f"{x+y}")
    return x+y
