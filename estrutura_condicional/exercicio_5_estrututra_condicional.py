# Uma determinada loja está fazendo promoções de vendas. Qualquer
# compra que um cliente fizer até R$ 100,00 receberá 5% de desconto. Se
# a compra for maior que R$ 100,00, mas inferior a R$ 200,00, o desconto
# será de 10%. Se for superior ou igual a R$ 200,00, o desconto será de
# 20%.
# Faça um programa que leia o quanto o cliente gastou e escreva o valor da
# conta já com os descontos.

valor = float(input("Digite o valor gasto: "))
total = 0

if valor < 100:
    total = valor - (valor*0.05)
elif valor > 100 and valor < 100:
    total = valor -(valor*0.10) 
else:
    total = valor - (valor*0.20)

print(f"O valor gasto foi de: R${valor:.2f}, com desconto: R${total:.2f}") 


