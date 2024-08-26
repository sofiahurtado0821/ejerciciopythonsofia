"""
En una llantera se ha establecido una promoción de las llantas marca "Todo Terreno", dicha promoción consiste en lo siguiente:
Si se compran menos de cinco llantas el precio es de $300.000 cada una, de $250.000 si se compran de cinco a 10 y de $200.000 si se compran más de 10.
"""
##Entrada de la cantidad de llantas a comprar
numerollantas=int(input("ingrese la cantidad de llantas que compro: "))
##Verificar la cantidad de llantas y determinar el precio por llanta
if numerollantas >= 10 :
    valorllanta= 200,000
elif 5< numerollantas >10 :
    valorllanta= (250000)
else:
    valorllanta= (300000)
##Mostrar resultados
print(f"el precio por llanta es: ${valorllanta:,}")
print(f"el costo total por {numerollantas}llantas es: ${valorllanta:,} ")
