#Faça um programa que mostre se é ano bicesto ou não

def eh_bissexto(ano):
    # Um ano é bissexto se for divisível por 4
    # Exceto se for divisível por 100, a menos que seja divisível por 400
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        return True
    else:
        return False

def main():
    # Solicita o ano do usuário
    ano = int(input("Digite um ano: "))
    
    # Verifica se é bissexto
    if eh_bissexto(ano):
        print(f"O ano {ano} é bissexto.")
    else:
        print(f"O ano {ano} não é bissexto.")

if __name__ == "__main__":
    main()
2024