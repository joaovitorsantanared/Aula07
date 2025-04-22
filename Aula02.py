N= int(input("Digite o número"))

if N >0 and N %2 ==0:
    print("Numero Positivo e Par")

elif N <0 and N %2 ==1:
    print("Numero Negativo e Impar")

elif N >0 and N %2 ==1:
    print("Numero Positivo e Impar")

elif N <0 and N %2 ==0:
    print("Numero Negativo e Par")

else:
    print("Numero inexistente") 