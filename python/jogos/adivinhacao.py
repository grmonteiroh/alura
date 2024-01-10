import random

def jogar():

    print("---------------------------------")
    print("Bem vindo ao jogo de adivinhação!")
    print("---------------------------------")

    numero_secreto = round(random.randrange(1,101))
    total_de_tentativas = 0
    pontos = 1000

    print("Qual nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Digite a dificuldade desejada: "))

    if(nivel == 1):
        total_de_tentativas = 20
    elif(nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 3

    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        chute = int(chute_str)
        print("Você digitou ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = numero_secreto == chute
        menor = numero_secreto > chute
        maior = numero_secreto < chute

        if(acertou):
            print("Você acertou!")
            print("Pontuação da partida: {}".format(pontos))
            break
        else:
            if(menor):
                print("Você errou! O seu chute foi menor do que o número secreto.")
            elif(maior):
                print("Você errou! O seu chute foi maior do que o número secreto.")
            pontos_perdidos = abs(numero_secreto-chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogar()