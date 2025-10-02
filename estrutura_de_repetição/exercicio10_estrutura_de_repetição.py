# Faça um programa que imprima os 20 primeiros números primos. 

cont = 2
qnt_primo = 0

while qnt_primo < 20:
    primo = True
    div = 2

    while div < cont:
        if cont % div==0:
            primo =False
        div +=1

    if primo:
        print(cont)
        qnt_primo +=1

    cont +=1
