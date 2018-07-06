import random

def jogar(): #como definir uma função no python

    imprime_msg_abertura()

    palavra_secreta = carrega_palavra_secreta()

    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    print(letras_acertadas)

    #for letra in palavra_secreta
    #letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    while(not enforcou and not acertou):
        
        chute = pega_chute()

        if (chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        imprime_msg_vencedor()
    else:
        imprime_msg_perdedor(palavra_secreta)


def imprime_msg_abertura():
    print("*******************************")
    print("Bem vindo ao jogo e advinhação!")
    print("*******************************")

def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()
    return palavra_secreta

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra] #isso funciona!

def pega_chute():
    chute = input("Qual letra? ")
    chute = chute.strip().upper() #método que tira os espaços digitados
    return chute

def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    #i comando palavra.find() não funciona porque ele para quando acha a primeira
    #letra procurada e ignora as repetidas, então se resolve com um for
    index = 0
    for letra in palavra_secreta:
        if(chute == letra): #método que deixa tudo em caps
            letras_acertadas[index] = letra
        index += 1
        
def imprime_msg_vencedor():
    print("Você acertou!")

def imprime_msg_perdedor(palavra):
    print("Você foi enforcado! A palavra era {}".format(palavra))
    
if(__name__ == "__main__"):
    jogar()
