import random

nome = input("Informe seu nome: ")
print(" Bem vindo",  nome, "vamos jogar!!")


while True :
    print("[1] PAR")
    print("[2] IMPAR")
    print("[3] SAIR")
    menu = int(input("ESCOLHA UMA OPÇÃO:  "))
    
    if menu == 1:
       valor = int(input('Digite um número [1 a 10] :'))
    elif menu == 2:
        valor = int(input('Digite um número [1 a 10] :'))
    elif menu == 3:
        break
    n_aleatorio = random.randint(1, 10)
    print("A maquina escolheu", n_aleatorio)
    
    soma = n_aleatorio + valor
    
    print("o valor foi: ", soma)
    
    if soma % 2 == 0:
        
        if menu == 1 :
            print(nome, "você ganhou")
        else:
            print(nome, "você perdeu")
            
    else:
        print("")
        
    
        if menu == 2 :
            print(nome, "você perdeu")
        else:
            print(nome, "você ganhou")
        
            
    
        
