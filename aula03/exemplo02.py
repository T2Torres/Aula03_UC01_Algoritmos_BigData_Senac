# Exemplo 02 (PDF disponível na pasta)

preco_unitario = input("Valor do ingresso: ") # (transformar texto em float)
preco_unitario = float(preco_unitario)

valor_disponivel = float(input("Valor disponível: "))
quantidade = int(valor_disponivel // preco_unitario) #Operação de divisão que mostra apenas o numero inteiro(sem virgulas)
troco = valor_disponivel % preco_unitario
print(f"Quantidade de ingressos: {quantidade}")
print(f"Troco de: R${troco}")