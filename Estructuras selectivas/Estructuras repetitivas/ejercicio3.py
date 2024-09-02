"""
Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos.
Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja
de todo el grupo
"""
# Inicializar variables
totalcalificaciones = 0
calificacionmaxima = 0
calificacionminima = 80

# Leer las calificaciones de los 20 alumnos
for i in range(20):
    while True:
        try:
            calificacion = float(input(f"Ingrese la calificación del alumno {i + 1}: "))
            if 0 <= calificacion <= 10:  # Suponiendo que las calificaciones están en el rango de 0 a 10
                break
            else:
                print("Por favor, ingrese una calificación válida entre 0 y 10.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número.")

    # Acumulando el total de calificaciones
    totalcalificaciones += calificacion

    # Determinar la calificación más alta y más baja
    if calificacion > calificacionmaxima:
        calificacionmaxima = calificacion
    if calificacion < calificacionminima:
        calificacion_minima = calificacion

# Calcular el promedio
promedio = totalcalificaciones / 20

# Imprimir resultados
print(f"Promedio de las calificaciones: {promedio:.2f}")
print(f"Calificación más alta: {calificacionmaxima:.2f}")
print(f"Calificación más baja: {calificacionminima:.2f}")