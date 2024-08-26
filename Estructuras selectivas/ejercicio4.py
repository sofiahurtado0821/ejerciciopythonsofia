"""En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un color que se escoge al azar. Si el color de la balota es rojo el descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si el color es diferente a los indicados no obtendrá descuento. Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar.
"""
nombre=input("ingrese su nombre y apellido")##pido que ingrese el nombre y apellido
colorbalota=input("digite el color de la balota(rojo,verde,otro):")##Entrada del color de la balota
##Entrada del monto total de la compra
valorcompra=int(input("digite el valor de la compra:"))
##Verificar el color de la balota y calcular el descuento
if colorbalota == "rojo" :
    descuento = 0.15 * valorcompra  ##15% de descuento si la balota es roja
elif colorbalota == "verde" :
    descuento = 0.20 * valorcompra  ##20% de descuento si la balota es verde
else:
    descuento = 0  ##Sin descuento si el color es diferente
##Calcular el valor a pagar
valorfinal=valorcompra - descuento
## Mostrar resultados
print(f"valor de la compra: ${valorcompra}")
print(f"color de la balota: {colorbalota}")
print(f"descuento aplicado: ${descuento}")
print(f"valor a pagar: ${valorfinal}")