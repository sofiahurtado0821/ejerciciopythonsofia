"""
En una llantera se ha establecido una promoción de las llantas marca "Todo Terreno", dicha promoción consiste en lo siguiente:
Si se compran menos de cinco llantas el precio es de $300.000 cada una, de $250.000 si se compran de cinco a 10 y de $200.000 si se compran más de 10.
"""
numerollantas=int(input("ingrese la cantidad de llantas que compro: "))
if numerollantas >= 10 :
    valorllanta= 200,000
elif 5< numerollantas >10 :
    valorllanta= (250000)
else:
    valorllanta= (300000)
print(f"el precio por llanta es: ${valorllanta:,}")
print(f"el costo total por {numerollantas}llantas es: ${valorllanta:,} ")
