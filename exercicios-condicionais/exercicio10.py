# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram
# para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério,
# baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R 280,00eR  700,00 : aumento de 15%
# salários entre R 700,00eR  1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.
salario = float(input("Digite o valor do salário: "))
if salario <= 280.00:
    n = 0.20
elif salario > 280 and salario <= 700:
    n = 0.15
elif salario > 700 and salario <= 1500:
    n = 0.10
elif salario > 1500:
    n = 0.05
aumento = n*salario
novoSalario = salario + aumento
print("Salário anterior: R$", salario)
print("Percentual do aumento: ", n*100, "%")
print("Valor do aumento: R$", aumento)
print("Novo salário: R$", novoSalario)