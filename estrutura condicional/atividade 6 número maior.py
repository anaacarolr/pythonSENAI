#atividade 6
#Solicite ao usuário um número de 1 a 7(representando um dia da semana) e exibao nome correspondente ao dia (por exemplo, 1 para "Domingo", 2 para "Segunda-feira", etc.).
num1 = int(input( " Digite um número: "))
num2 = int(input( " Digite outro número: "))
num3 = int(input( " Digite outro número2: "))
if num1 > num2 :
    if num1 > num3 :
        verificada = "numero 1 é maior"
       
        print("o numero 1 é maior ")
   
elif num2 > num1 :
    if num2 > num3 :
        verificada = "numero 2 é maior"
   
    print("o numero 2 é maior ")
   
if num3 > num1 :
    if num3 > num2 :
        verificada = "numero 3 é maior"
   
    print("o numero 3 é maior ")
