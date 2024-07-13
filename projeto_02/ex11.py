#Crie um jogo papel pedra tesoura e jogue com o computador#


import random

def play():
    user = input("Qual sua escolha? 'r' para pedra, 'p' para papel, 's' para tesoura: ")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "É um empate!"

    if is_win(user, computer):
        return "Você ganhou!"

    return "Você perdeu!"

def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
    return False

print(play())


