"""determinar  si un aprendiz aprueba o desaprueba algoritmia, sabeindo que aprobara si su promedio de tres 
calificaciones es mayo o igual a 70; reprueba en caso contrario
"""
nombre=input("diite el nombre del estudiante:")
calificacion1=int(input("digite su calificacion1:"))
calificacion2=int(input("digite su calificacion:"))
calificacion3=int(input("digite su calificacion:"))
promedio=(calificacion1+calificacion2+calificacion3)/3
if promedio >=70 :
    print("el estudiante aprobo")
else :
    print("el estudiante desaprobo")




