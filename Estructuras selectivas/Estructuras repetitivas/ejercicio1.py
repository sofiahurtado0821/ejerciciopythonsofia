"""
Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos
neutros
"""
##definiendo variables
positivos = 0
negativos = 0
neutros = 0
for i in range(20):
    numeros = int(input("ingrese un numeros:"))
    if numeros > 0:
        positivos +=1
    elif numeros < 0:
        negativos += 1
    else:
        neutros += 1
## imprimir los resultados 
print(f'Los numeros positivos son: {positivos} los numeros negativos son: {negativos} los numeros neutros son: {neutros}')
    
