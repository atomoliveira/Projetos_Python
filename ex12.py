
import math

nome_solucao = input("Digite o nome da solução :")
concentracao_H = float(input("Digite a concentração de ions de hidrogênio(em mol/L)"))
pH = - math.log10(concentracao_H)
print(f"O pH da solução {nome_solucao} é {pH:2f}")

