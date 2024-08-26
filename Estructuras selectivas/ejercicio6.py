"""
Se ha establecido un programa para estimular a los alumnos, el cual consiste en lo siguiente: si el promedio obtenido por un alumno en el último periodo es mayor o 
igual que 4.0, se le hará un descuento del 30% sobre la pensión; si el promedio obtenido es menor que 4.0 deberá pagar la pensión completa, la cual incluye el 10% de 
IVA. Obtener cuanto debe pagar un alumno.
"""
##Entrada del promedio obtenido
promedio=int(input("ingrese su promedio:"))
pension=int(input("ingrese el valor de su pension:"))##Entrada del valor de la pensión
##Verificar el promedio y calcular el descuento
if promedio >=40 :
    descuento= pension * 0.30
    valortotal= pension - descuento 
else:
    iva= pension * 0.01
    valortotal= pension + iva 
##Mostrar resultados
print(f"el valor total que debe pagar el estudiante es de: ${valortotal}")