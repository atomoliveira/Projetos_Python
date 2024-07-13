#Escreva um programa que monte a tabela Fibinacci#

def tabela_fibonacci(n):
    fibonacci = [0, 1]
    for i in range(2, n):
        fibonacci.append(fibonacci[i-1] + fibonacci[i-2])
    return fibonacci

print(tabela_fibonacci(50))