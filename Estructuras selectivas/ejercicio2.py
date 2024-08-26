"""Calcular el total a pagar por la compra de zapatillas. Si se compran tres o más zapatillas se aplica un descuento del 20% sobre el total de la compra y si son menos de tres zapatillas un descuento del 10%. Mostrar en pantalla, el valor de la compra, el valor del descuento y el valor a pagar una vez aplicado el descuento
"""
numeroZapatilla=int(input("Digite la cantidad de zapatillas:"))##Aqui pido la cantidad de zapatillas
valorCompra=int(input("Digite el valor total de la compra:"))##Aqui pido el valor total de las zapatillas
if numeroZapatilla >=3 : ##mostrar resultados
    descuento1= valorCompra * (20/100)
    valorFinal = valorCompra - descuento1 ##primer descuento
    print(f"el valor de la compra con el descuento 20% es {valorFinal}")
elif numeroZapatilla < 3 :
    descuento2= valorCompra * (10/100)
    valorFinal= valorCompra - descuento2 ##segundo descuento
    print(f"el valor de la compra con el descuento 10% es {valorFinal}")
else :
    print=(f"no ingreso correctamente los datos")



