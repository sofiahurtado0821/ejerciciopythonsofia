"""En un supermercado se hace una promoción, mediante la cual el cliente obtiene un descuento dependiendo de un color que se escoge al azar. Si el color de la balota es rojo el descuento es del 15% sobre el total de la compra, la balota es verde el descuento es del 20%. Si el color es diferente a los indicados no obtendrá descuento. Imprimir el valor de la compra, el color de la balota, el descuento y el valor a pagar.
"""
nombre=input("ingrese su nombre y apellido")
colorbalota=input("digiteel color de la balota(rojo,verde,otro):")
valorcompra=int(input("digite el valor de la compra:"))

if colorbalota == "rojo" :
    descuento = 0.15 * valorcompra
elif colorbalota == "verde" :
    descuento = 0.20 * valorcompra
else:
    descuento = 0
valorfinal=valorcompra - descuento
print(f"valor de la compra: ${valorcompra}")
print(f"color de la balota: {colorbalota}")
print(f"descuento aplicado: ${descuento}")
print(f"valor a pagar: ${valorfinal}")