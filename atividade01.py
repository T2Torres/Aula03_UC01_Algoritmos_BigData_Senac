#Atividade 03 no pdf

salario_atual = float(input(f"Informe o salário: R$"))
reajuste = salario_atual * 0.18

novo_salario = salario_atual + reajuste

print(30*"=")
print(f"Salário inicial: R${salario_atual:.2f}")
print(f"Valor do reajuste: R${reajuste:.2f}")
print(f"Salário reajustado: R${novo_salario:.2f}")