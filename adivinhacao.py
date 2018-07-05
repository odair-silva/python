import random #biblioteca para utilizar a função 'random'

print("*******************************")
print("Bem vindo ao jogo e advinhação!")
print("*******************************")

numero_secreto = random.randrange(1,101)
total_de_tentativas = 3

print(numero_secreto)

for rodada in range(1, total_de_tentativas + 1):
    print("Tentativa {} de {}". format(rodada, total_de_tentativas))
    chute_str = input("Digite um número entre 1 e 100: ") #input retorna sempre string
    chute = int(chute_str) #converte para int
    print("Você digitou ", chute_str)

    if(chute < 1 or chute > 100):
        print("Você deve digitar um número entre 1 e 100")
        continue #entra no proximo loop do for

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto
    
    if (acertou):
        print("Você acertou")
        break #sai do for
    else:
        if(maior):
            print("Você errou! O seu chute foi acima do valor secreto.")
        if(menor):
            print("Você errou! O seu chute foi abaixo do valor secreto.")

print("Fim do Jogo :(")


