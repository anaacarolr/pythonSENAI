def input_str(mensagem):
    while True:
        nome = str(input(mensagem))
        
        
        if not nome.isalpha():
            print("digite apenas letras")
        else:
            return nome

def input_int(mensagem):
    while True:
        try :
            num = int(input(mensagem))
            return num
        except ValueError :
            print("digite apenas números")
            
def input_float(mensagem):
    while True :
        try :
            num1 = float(input(mensagem))
            return num1
        except ValueError :
            print("digite apenas números")
            
        