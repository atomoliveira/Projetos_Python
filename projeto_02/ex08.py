#Faça um programa que apartir da data mostre quanto falta para o fim do ano 

from datetime import datetime

def dias_ate_fim_do_ano(data_atual):
    # Define a data do final do ano
    fim_do_ano = datetime(data_atual.year, 12, 31)
    
    # Calcula a diferença entre a data do final do ano e a data atual
    diferenca = fim_do_ano - data_atual
    
    return diferenca.days

def main():
    # Obtém a data atual
    data_atual = datetime.now()
    
    # Calcula os dias até o fim do ano
    dias_restantes = dias_ate_fim_do_ano(data_atual)
    
    # Exibe o resultado
    print(f"Faltam {dias_restantes} dias para o fim do ano.")

if __name__ == "__main__":
    main()
