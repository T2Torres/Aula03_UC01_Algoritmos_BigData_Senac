# GitHub
print("Gitub - Aula 03")

# Exemplo01 - Veículo 10 km/l
# Entrada
CONSUMO = 10        #variavel em letra maiúscula se chama CONSTANTE (valor que não vai mudar)
distancia1 = float(input("Informe a distância: "))    #100
distancia2 = float(input("Informe a outra distância: "))  #50

# Processamento
distancia_total = distancia1 + distancia2
combustivel = distancia_total / CONSUMO

print(f'Distância percorrida {distancia_total}')
print(f"Consumo de {combustivel} litros")