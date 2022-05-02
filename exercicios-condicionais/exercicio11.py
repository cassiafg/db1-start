# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
# que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a
# 11% do Salário Bruto, mas não é descontado (é a empresa que deposita).
# O Salário Líquido corresponde ao Salário Bruto menos os descontos.
#O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.#
# Desconto do IR:
# Salário Bruto até 900 (inclusive) – isento
# Salário Bruto até 1500 (inclusive) – desconto de 5%
# Salário Bruto até 2500 (inclusive) – desconto de 10%
# Salário Bruto acima de 2500 – desconto de 20% Imprima na tela as informações
valorHora = float(input("Digite o valor da sua hora: "))
horasTrabalhadas = float(input("Digite a quantidade de horas trabalhadas: "))
salarioBruto = valorHora * horasTrabalhadas
if salarioBruto <= 900:
    ir = 0
if salarioBruto > 900 and salarioBruto <= 1500:
    ir = 0.05
if salarioBruto > 1500 and salarioBruto <= 2500:
    ir = 0.10
if salarioBruto > 2500:
    ir = 0.20
descontoSindicato = salarioBruto*0.03
descontoIR = salarioBruto*ir
salarioLiquido = salarioBruto - descontoSindicato - descontoIR
print("--------------------------------------")
print("Salário Bruto: R$", salarioBruto)
print("--------------------------------------")
print("--------------Descontos---------------")
print("Sindicato: R$", descontoSindicato)
print("IR: R$", descontoIR)
print("--------------------------------------")
print("Salário Líquido: R$", salarioLiquido)
print("FGTS depositado: R$", salarioBruto*0.11)