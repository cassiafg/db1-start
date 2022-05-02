# Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
prod1 = float(input("Digite o preço do produto 1: "))
prod2 = float(input("Digite o preço do produto 2: "))
prod3 = float(input("Digite o preço do produto 3: "))
menor = prod1
if prod2 < menor:
    menor = prod2
if prod3 < menor:
    menor = prod3
print("Você deve comprar o produto que custa ", menor)