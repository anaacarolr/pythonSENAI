#construa um programa que solicite um nome de um produto e o preço,  aplique um desconto de 5%, exiba o novo opreço do produto e quanto ele diminuiu
 
 # passo 1: qual é o resultado que vc quer?
#exivbir o novo preço do produto e quanto ele diminuiu
 
 #passo 2: o que eu preciso de informação para chegar nesse resultado?
 #ter o preço do produto, aplicar os 5% de desconto e o valor final, e o quanto ficou mais barato
 
 #passo 3: qual é o passa a passo para fazer o que você quer?
 #ter o preço do produto, fazer a divisão para saber o 5% de desconto e subtrair com o valor no final para saber o qaunto ele diminuiu.
 
print("desconto de produto ")

nome =input("escreva o nome do produto")
produto= int(input("digite o preço do produto "))
resultado = produto / 5
resultado2 =produto - resultado

print("o novo preço será:", resultado, "e o quanto ele diminuiu foi: ", resultado2)


