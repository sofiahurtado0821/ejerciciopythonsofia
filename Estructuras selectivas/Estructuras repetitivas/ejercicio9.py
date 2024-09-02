"""
Calcular el promedio de edades de hombres, mujeres y de todo un grupo de alumnos
"""
# Inicializar variables
sumaEdadesHombres = 0
sumaEdadesMujeres = 0
contadorHombres = 0
contadorMujeres = 0
# Leer la cantidad de alumnos
n = int(input("Ingrese la cantidad total de alumnos: "))
# Leer el sexo y la edad de los alumnos
for i in range(n):
 sexo = input("Ingrese el sexo del alumno (M para hombre, F para mujer): ").upper()
 edad = int(input("Ingrese la edad del alumno: "))

 if sexo == 'M':
     sumaEdadesHombres += edad
     contadorHombres += 1  
 elif sexo == 'f':

     sumaEdadesMujeres += edad
     contadorMujeres += 1
# Calcular promedios
promedioHombres = sumaEdadesHombres / contadorHombres if contadorHombres > 0 else 0
promedioMujeres = sumaEdadesMujeres / contadorMujeres if contadorMujeres > 0 else 0
promedioGrupo = (sumaEdadesHombres + sumaEdadesMujeres) / n if n > 0 else 0
# Imprimir resultados
print(f"Promedio de edad de los hombres: {promedioHombres}")
print(f"Promedio de edad de las mujeres: {promedioMujeres}")
print(f"Promedio de edad del grupo: {promedioGrupo}")
