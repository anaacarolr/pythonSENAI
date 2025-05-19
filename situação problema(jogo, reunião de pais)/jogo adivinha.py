# JOGO DE ADIVINHAÇÃO
import random
nome = input("Informe seu nome: ")
print(nome, "Bem vindo ao jogo de Adivinhação!")
print("Como jogar? a maquina irá escolher um numero secreto e você vai ter que adivinhar qual número a maquina escolheu")
numero_secreto = random.randrange(1,100)

    
while True :           
    escolha = int(input('Digite um número: '))
    if escolha < numero_secreto :
        print("o numero que você escolheu é menor que o número secreto")
    elif escolha > numero_secreto :
        print("o numero que você escolheu é maior que o número secreto")
    else:
       print("parabens vc acertou ")
       print("deseja continuar? ")
       print("[1] - sim ")
       print("[2] - não ")
       opcao = int(input("escolha uma opção "))
       if opcao == 1:
           print("vamos para uma nova rodada, lets gooooo ")
           numero_secreto = random.randrange(1,100)
       else:
           break

  
          