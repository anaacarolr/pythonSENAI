import inputs

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
            
    print("[1] MULTIPLICAÇÃO")
    print("[2] ADIÇÃO")
    print("[3] DIVISÃO")
    print("[4] SUBTRAÇÃO")
    print("[5] TODAS AS OPÇÕES")
    
    
    opcao = inputs.input_int("escolha uma opção:")
    if opcao > 5 or opcao < 1:
        print("essa opção não existe!!")
    numero1 = inputs.input_int("digite um número:")

    numero2 = inputs.input_int("digite outro número:")   


    if opcao == 2: 
        print("Adição = ",adicao(numero1, numero2))
    
    elif opcao == 1 :
        print("multiplicação = ", multiplicacao(numero1, numero2))
    
    elif opcao == 3 :
        print("divisão = ", divisao(numero1, numero2))
    
    elif  opcao == 4 :
        print("subtração = ", subtracao(numero1, numero2))

    elif opcao == 5 :
        print("Contas = ")
        mostrar_contas(numero1, numero2)
            
while True:
    menu_calculadora()