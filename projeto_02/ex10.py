# Faça um programa que crie uma inteface grafica simples de uma calculador

import tkinter as tk

# Função para calcular a expressão matemática
def calcular(expressao):
    try:
        resultado = eval(expressao)
        return resultado
    except Exception as e:
        return "Erro"

# Função chamada quando o botão "=" é pressionado
def on_equal_press():
    expressao = entrada.get()
    resultado = calcular(expressao)
    entrada.delete(0, tk.END)
    entrada.insert(tk.END, str(resultado))

# Função chamada quando um botão de número ou operador é pressionado
def on_button_press(valor):
    entrada.insert(tk.END, valor)

# Função chamada quando o botão "C" (clear) é pressionado
def on_clear_press():
    entrada.delete(0, tk.END)

# Configuração da janela principal
janela = tk.Tk()
janela.title("Calculadora Simples")

# Campo de entrada para a expressão matemática
entrada = tk.Entry(janela, width=20, font=('Arial', 18))
entrada.grid(row=0, column=0, columnspan=4)

# Botões da calculadora
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
    ('C', 5, 0)
]

# Criação e posicionamento dos botões
for (texto, linha, coluna) in botoes:
    botao = tk.Button(janela, text=texto, width=5, height=2, font=('Arial', 18))
    botao.grid(row=linha, column=coluna, sticky='nsew')
    if texto == '=':
        botao.config(command=on_equal_press)
    elif texto == 'C':
        botao.grid(columnspan=4)
        botao.config(command=on_clear_press)
    else:
        botao.config(command=lambda valor=texto: on_button_press(valor))

# Inicia o loop principal da aplicação
janela.mainloop()
