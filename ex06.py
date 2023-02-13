#faça um programa que mostre a taxa de IMC , quando o usuario entra com os dados

peso =float(input("Digite o seu peso em  KG:"))
altura=float(input("Digite a sua altura em metro:"))

imc= peso/(altura*altura)
print(imc)

if (imc < 18.5):
    print("Abaixo do peso")
elif(imc < 25):
    print("Peso Normal")
elif(imc < 30):
    print("Sobrepeso")
elif(imc < 35):
    print("Obesidade grau 1")
elif(imc <40):
    print("Obesidade grau 2")
else :
    print("Obesidade grau 3")
