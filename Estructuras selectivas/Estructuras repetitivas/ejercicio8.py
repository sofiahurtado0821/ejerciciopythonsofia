"""
un grupo de 23 estudiantes presentan un examen de algoritmia. Hacer un
algoritmo que lea por cada estudiante la calificación obtenida
"""
# Inicializar variables
contadorMenos50 = 0
contador50a69 = 0
contador70a79 = 0
contador80oMas = 0
# Leer las calificaciones de 23 estudiantes
for i in range(23):
 calificacion = int(input("Ingrese la calificación del estudiante (1 a 100): "))

 if calificacion < 50:
  contadorMenos50 += 1
 elif calificacion < 70:
  contador50a69 += 1
 elif calificacion < 80:
  contador70a79 += 1
 else:
  contador80oMas += 1
# Imprimir resultados
print(f"Estudiantes con calificación menor a 50: {contadorMenos50}")
print(f"Estudiantes con calificación entre 50 y 69: {contador50a69}")
print(f"Estudiantes con calificación entre 70 y 79: {contador70a79}")
print(f"Estudiantes con calificación de 80 o más: {contador80oMas}")
