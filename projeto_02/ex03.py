#Sabendo que uma milha marítima equivale a um mil, oitocentos e cinquenta e dois metros 
# e que um quilômetro possui mil metros, 
# fazer um programa para converter milhas marítimas em quilômetros.

def milhas_maritimas_para_km(milhas_maritimas):
    # Definindo a constante de conversão
    metros_por_milha_maritima = 1852
    metros_por_km = 1000

    # Convertendo milhas marítimas para metros
    metros = milhas_maritimas * metros_por_milha_maritima

    # Convertendo metros para quilômetros
    quilometros = metros / metros_por_km

    return quilometros

# Exemplo de uso:
milhas_maritimas = float(input("Digite a quantidade de milhas marítimas: "))
quilometros = milhas_maritimas_para_km(milhas_maritimas)
print(f"{milhas_maritimas} milhas marítimas equivalem a {quilometros:.2f} quilômetros")
