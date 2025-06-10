'''
A temperatura ideal para a qualidade do ar é entre 20c e 22c no inverno e 23c e 26c no verão
A umidade ideal para a saúde humana deve estar entre 40% e 55% no inverno e 40% e 65% no verão.
Faça uma função que verifica a qualidade do ar com base nesses dados.
'''

def verificar_inverno(qualidade):
    if graus >= 20 and graus =< 22 :
        print("A qualidade do ar está boa")
    else:
        print("A qualidade do ar está ruim")
            
def verificar_verao(ar):
    if graus >= 23 and graus =< 26 :
        print("A qualidade do ar está boa")
    else:
        print("A qualidade do ar está ruim")

estação = int( " Digite a estação [ INVERNO(1) ou VERÃO(2) ]: ")
graus = int(input( " Digite a temperatura: "))
umidade = int(input( " Digite a umidade: "))

if estação == 1:
    verificar_inverno()
else:
    verificar_verao()