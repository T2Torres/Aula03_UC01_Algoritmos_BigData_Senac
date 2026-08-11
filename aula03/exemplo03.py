#Entrada
preco = float(input(f"Preço do Produto: "))
quantidade = int(input(f"Quantidade Comprada: "))
#Processamento
total = preco * quantidade
desconto = total * 0.1 #desconto de 10%
valor_pagar = total- desconto

print(30*"=")
print(f"Valor total R$ {total:.2f}")
print(f"Desconto de R$ {desconto:.2f}")
print(f"Valor final: R${valor_pagar:.2f}")




