# 3 - Calculador de despesas: Desenvolva um programa com um menu que de acordo com a escolha do usuário ele consiga, adicionar um valor de uma despesa ou exibir o valor total dessas contas e encerrar.

# [0] Sair

# [1] Adicionar valor da despesa

# [2] Mostrar a quantidade e o valor total das despesas

print("Despesas")

valor = 0
n_despesas = 0

while True:
    print("Despesas")
    print("[1] Valor da despesa")
    print("[2] Quantidade e valor total da despesa")
    print("[0] Sair")
    menu = int(input("ESCOLHA UMA OPÇÃO:  "))
    if menu == 0:
        print("Você saiu")
        break
    elif menu == 1:
        ad_valor = int(input("DIGITE O VALOR DA SUA DESPESA "))
        print(ad_valor, "ADICIONADO NAS DESPESAS")
        n_despesas += 1
        valor = ad_valor + valor
       
    elif menu == 2:
        print("TOTAL ", n_despesas, "DESPESAS, SOMANDO", valor, "REAIS DE DESPESAS")
       
    else:
        print("ERRO")
    
    