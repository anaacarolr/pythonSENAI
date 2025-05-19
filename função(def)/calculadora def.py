# 3 - Calculadora Básica: Crie uma função que receba dois números como parâmetros e exiba o resultado das operações básicas de adição, subtração, multiplicação e divisão.

# 3.1 - Crie uma função que receba dois números como parâmetros para cada uma das operações básicas citadas acima retornando somente o valor das operações. 

# 3.2 - Crie uma função que faça um menu para o usuário escolher a opção desejada.



def adicao(numero1, numero2) :
    return numero1 + numero2
    
def subtracao(numero1, numero2) :
    return numero1 - numero2
    
def multiplicacao(numero1, numero2) :
    return numero1 * numero2
    
def divisao(numero1, numero2): 
    return numero1 / numero2

def mostrar_contas(n1, n2) :
    print("a conta usando adição é", adicao(n1, n2))
    print("a conta usando subtração é", subtracao(n1, n2))
    print("a conta usando multiplicação é", multiplicacao(n1, n2))
    print("a conta usando divisão é", divisao(n1, n2))
    
def menu_calculadora():
    numero1 = float(input("DIGITE UM NÚMERO: "))
    numero2 = float(input("DIGITE OUTRO NÚMERO: "))
    
    print("[1] MULTIPLICAÇÃO")
    print("[2] ADIÇÃO")
    print("[3] DIVISÃO")
    print("[4] SUBTRAÇÃO")
    print("[5] TODAS AS OPÇÕES")
    
    opcao = int(input("ESCOLHA UMA OPÇÃO: "))
    if opcao == 2: 
        print("Adição = ",adicao(numero1, numero2))
        
    elif opcao == 1 :
        print("multiplicação = ", multiplicacao(numero1, numero2))
        
    elif opcao == 3 :
        print("divisão = ", divisao(numero1, numero2))
        
    elif  opcao == 4 :
        print("subtração = ", subtracao(numero1, numero2))
    
    elif opcao == 5 :
        print("Contas = ", mostrar_contas(numero1, numero2))

menu_calculadora()  
