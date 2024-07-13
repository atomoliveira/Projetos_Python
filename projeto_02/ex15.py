#Faça um programa que ao entrar com a porcentagem de a datação de uma ossada por carbono-14

import math

def calcular_idade_carbono14(percentual_restante, meia_vida=5730):
    # Constante de decaimento
    lambda_c14 = math.log(2) / meia_vida
    
    # Calcula a idade
    idade = math.log(percentual_restante) / -lambda_c14
    
    return idade

def main():
    # Solicita a porcentagem de Carbono-14 restante do usuário
    percentual_restante = float(input("Digite a porcentagem de Carbono-14 restante (em %): ")) / 100
    
    # Calcula a idade da ossada
    idade_ossada = calcular_idade_carbono14(percentual_restante)
    
    # Exibe o resultado
    print(f"A idade da ossada é aproximadamente {idade_ossada:.2f} anos.")

if __name__ == "__main__":
    main()
