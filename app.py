# Programa que calcula o valor do desconto de uma compra

# Entrada:
print("  ")
valor_compra= float(input("Digite o valor da compra: R$ "))

# Processamento:
if valor_compra>=300.00:
    percentual_desconto=0.15
    print("Desconto de 15%")
elif valor_compra>=200.00:
    percentual_desconto=0.10
    print("Desconto de 10%")
else:
    percentual_desconto=0.05
    print("Desconto de 5%")

# Calculo do Valor do desconto
valor_desconto=(valor_compra*percentual_desconto)

# Calculo valor a pagar:
valor_final=(valor_compra-valor_desconto)

# Saída:
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Valor da compra a pagar: R$ {valor_final:.2f}")
print("====================================")
print(" ")
print("Obrigado por comprar conosco!")
print("VOLTE SEMPRE!")
print(" ")
