print("*******************************")
print("Bem vindo ao jogo e advinhação!")
print("*******************************")


numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu número: ") #input retorna sempre string
    chute = int(chute_str) #converte para int
    print("Você digitou ", chute_str)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    
    if (acertou):
        print("Você acertou")
        rodada = 3
    else:
        if(maior):
            print("Você errou! O seu chute foi acima do valor secreto.")
        if(menor):
            print("Você errou! O seu chute foi abaixo do valor secreto.")
    rodada = rodada + 1

print("Fim do Jogo :(")


