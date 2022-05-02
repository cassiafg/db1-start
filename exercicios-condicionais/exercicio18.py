#Faça um Programa que leia um número inteiro menor que 1000 
# e imprima a quantidade de centenas, dezenas e unidades do mesmo
num = int(input("Digite um número inteiro menor que 1000: "))
#extraindo a unidade
unidade = num % 10
#eliminando a unidade do número
num = (num - unidade) / 10
#extraindo a dezena
dezena = num % 10
num = (num - dezena) / 10
centena = num
#transformando em inteiros
dezena = int(dezena)
centena = int(centena)
print("O número tem ", centena, "centenas, ", dezena, " dezenas e ", unidade, " unidades.")
