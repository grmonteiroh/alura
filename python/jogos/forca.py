import random

def msg_abertura():
    print("---------------------------------")
    print("Bem vindo ao jogo de forca!")
    print("---------------------------------")
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        palavras.append(linha.strip())

    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    return palavra_secreta
def inicializa_letras_acertadas(palavra):
    letras_acertadas = ["_" for letra in palavra]
    return letras_acertadas
def pede_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper()
    return chute
def marca_chute_correto(palavra_secreta, chute, letras_acertadas):
    index = 0
    for letra in palavra_secreta:
        if (chute.upper() == letra.upper()):
            letras_acertadas[index] = letra
        index += 1
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()
def imprime_msg_vitoria(palavra_secreta):
    print("\nVocê ganhou!!! Tu é o bixão!!")
    print("Leve esse(a) {} de recomepnsa!!".format(palavra_secreta))
def imprime_msg_derrota(palavra_secreta):
    print("\nVocê perdeu! PATO! QUACK QUACK!")
    print("A palavra correta era {}.".format(palavra_secreta))
def jogar():
    msg_abertura()
    palavra_secreta = carrega_palavra_secreta()
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        print(letras_acertadas)
        chute = pede_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(palavra_secreta, chute, letras_acertadas)
        else:
            erros += 1
            desenha_forca(erros)
            if(erros < 7):
                print("Você ainda tem {} tentativas".format(7 - erros))

        enforcou = (erros == 7)
        acertou = "_" not in letras_acertadas

    if(acertou):
        imprime_msg_vitoria(palavra_secreta)
    else:
        imprime_msg_derrota(palavra_secreta)

if(__name__ == "__main__"):
    jogar()