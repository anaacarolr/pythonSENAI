#Solicite um número ao usuario e exiba todos os números pares e a quantidade deles até o número é solicitado
num = int(input("Digite um numero: "))
quantidade = 0

print(num)

while True :
    num = num - 1
    if num % 2 == 0 :
        print(num)
        quantidade = quantidade + 1
    elif num <= 0 :
        print("a quantidade de numeros pares é", quantidade + 1)
        
        break 