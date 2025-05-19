#construa um programa que solicite um salário, aplique um aumento de  10 %, exiba seu novo salário e quanto ele aumentou 


#passo 1: qual é o resultado que vc quer?
#exibir o novo salário depois do 10% de aumento

#passo 2: o que eu preciso de informação para chegar nesse resultado?
#o salário e os 10% dele

#passo 3: qual o passo a passo para fazer o que você quer?
#calcular o 10% do salário em questão e depois fazer uma adição somando os 10% com o salario, assim exibindo o novo salário

print("aumento do salario ")

salario = int(input("digite o salario "))
resultado = salario * 10
resultado2 = resultado/100

print("o aumento foi de ", resultado2, "e o novo salario é ", resultado2 + salario)

