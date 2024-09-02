"""
Una persona debe realizar un muestreo con 50 personas para determinar el
promedio de peso de los niños, jóvenes, adultos y ancianos que existen en su zona
"""
## inicializar variables
pesoNiños = 0
pesoJovenes = 0
pesoAdultos = 0
pesoAncianos = 0


contadorNiños = 0
contadorJovenes = 0
contadorAdultos = 0
contadorAncianos = 0

## leer peso y edad de 50 personas

for i in range(50):
    edad = int(input("ingrese la edad de la persona: "))
    peso = int(input("ingrese el peso de la persona: "))

    if edad <= 12:
        pesoNiños += peso
        contadorNiños += 1
    elif edad <= 29:
        pesoJovenes += peso
        contadorJovenes += 1
    elif edad <59:
        pesoAdultos += peso
        contadorAdultos += 1
    else:
        pesoAncianos += peso
        contadorAncianos += 1
    
    ##calcular promedios 
    promedioPesoNinos =  pesoNiños / contadorNiños  if contadorNiños > 0 else 0
    promedioPesoJovenes = pesoJovenes / contadorJovenes if contadorJovenes > 0 else 0
    promedioPesoAdultos = pesoAdultos / contadorAdultos if contadorAdultos > 0 else 0
    promedioPesoAncianos = pesoAncianos / contadorAncianos  if contadorAncianos > 0 else 0

## imprimir resultados 
print(f"El promedio de peso de los niños es: {promedioPesoNinos} kg")
print(f"El promedio de peso de los jóvenes es: {promedioPesoJovenes} kg")
print(f"El promedio de peso de los adultos es: {promedioPesoAdultos} kg")
print(f"El promedio de peso de los ancianos es: {promedioPesoAncianos} kg")