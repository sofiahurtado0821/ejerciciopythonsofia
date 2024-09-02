"""
Pedir los datos de los alumnos, estos son: sexo, edad y altura. Al final del programa
se deberá mostrar la cantidad de hombres, la cantidad de mujeres, la altura promedio
,la cantidad de alumnos que tienen una altura mayor a 1.70 cm, la cantidad de alumnos
que tiene una altura menor o igual a 1.50 cm. El programa debe finalizar cuando la edad
sea igual a 0.
"""
# Inicializar variables
contadorHombres = 0
contadorMujeres = 0
sumaAlturas = 0
contadorAlturaMayor170 = 0
contadorAlturaMenorIgual150 = 0
# Leer datos de alumnos
while True:
 sexo = input("Ingrese el sexo del alumno (M para hombre, F para mujer): ").upper()
 edad = int(input("Ingrese la edad del alumno (0 para finalizar): "))
 if edad == 0:
   break
 altura = float(input("Ingrese la altura del alumno en metros: "))

 if sexo == 'M':
  contadorHombres += 1
 elif sexo == 'F':
  contadorMujeres += 1

 sumaAlturas += altura
 if altura > 1.70:
  contadorAlturaMayor170 += 1
 if altura <= 1.50:
  contadorAlturaMenorIgual150 += 1
# Calcular promedios
cantidadAlumnos = contadorHombres + contadorMujeres
promedioAltura = sumaAlturas / cantidadAlumnos if cantidadAlumnos > 0 else 0
# Imprimir resultados
print(f"Cantidad de hombres: {contadorHombres}")
print(f"Cantidad de mujeres: {contadorMujeres}")
print(f"Altura promedio del grupo: {promedioAltura:.2f} metros")
print(f"Cantidad de alumnos con altura mayor a 1.70 m: {contadorAlturaMayor170}")
print(f"Cantidad de alumnos con altura menor o igual a 1.50 m: {contadorAlturaMenorIgual150}")