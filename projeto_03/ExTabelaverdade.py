#Faça um programa que gere a Tabela Verdade

# Função para imprimir a tabela verdade
def tabela_verdade():
    # Cabeçalho da tabela
    print("--------------------------------------")
    print("        TABELA VERDADE                ")
    print("--------------------------------------")
    print("----------------------------------------")
    print("A | B | A AND B | A OR B | NOT A | NOT B")
    print("----------------------------------------")

    # Lista de valores verdade (True) e falso (False)
    valores = [False, True]

    # Geração da tabela verdade
    for A in valores:
        for B in valores:
            and_result = A and B
            or_result = A or B
            not_a = not A
            not_b = not B
            print(f"{A} | {B} |   {and_result}   |  {or_result}  |  {not_a}  |  {not_b}")

# Chama a função para imprimir a tabela verdade
tabela_verdade()
