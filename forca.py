import random

def jogar(): #como definir uma função no python

    print("*******************************")
    print("Bem vindo ao jogo e advinhação!")
    print("*******************************")

    arquivo = open("palavras.txt", "r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    letras_acertadas = ["_" for letra in palavra_secreta] #isso funciona!

    #for letra in palavra_secreta
    #letras_acertadas.append("_")

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper() #método que tira os espaços digitados

        if (chute in palavra_secreta):
            #i comando palavra.find() não funciona porque ele para quando acha a primeira
            #letra procurada e ignora as repetidas, então se resolve com um for
            index = 0
            for letra in palavra_secreta:
                if(chute == letra): #método que deixa tudo em caps
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops, você errou! Faltam {} tentativas.".format(6-erros))

        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Você acertou!")
    else:
        print("Você perdeu!")
        
    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()
