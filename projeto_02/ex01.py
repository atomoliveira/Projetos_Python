#Fazer um programa para entrar via teclado com o valor da primeira nota (P1) 
# e o programa deverá calcular e exibir quanto o aluno precisa tirar na segunda nota (P2) 
# para ser aprovado, sabendo que a média de aprovação é igual a seis.

# Solicita a entrada do valor da primeira nota (P1)
P1 = float(input("Digite a nota da primeira prova (P1): "))

# Calcula a nota necessária na segunda prova (P2)
P2 = 12 - P1

# Exibe a nota necessária na segunda prova (P2)
print(f"Para ser aprovado, você precisa tirar {P2:.2f} na segunda prova (P2).")