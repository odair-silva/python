def jogar(): #como definir uma função no python

    print("*******************************")
    print("Bem vindo ao jogo e advinhação!")
    print("*******************************")

    palavra_secreta = "pedante"
    letras_acertadas = ["_","_","_","_","_","_","_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip() #método que tira os espaços digitados

        #i comando palavra.find() não funciona porque ele para quando acha a primeira
        #letra procurada e ignora as repetidas, então se resolve com um for
        index = 0
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()): #método que deixa tudo em caps
                letras_acertadas[index] = letra
            index = index + 1
        print(letras_acertadas)

    print("Fim de jogo!")

if(__name__ == "__main__"):
    jogar()