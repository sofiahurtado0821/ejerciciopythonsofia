"""determinar  si un aprendiz aprueba o desaprueba algoritmia, sabeindo que aprobara si su promedio de tres 
calificaciones es mayo o igual a 70; reprueba en caso contrario
"""
nombre=input("diite el nombre del estudiante:")##Pido el nombre del estudiante
calificacion1=int(input("digite su calificacion1:"))##El estudiante debe ingresar su primera calificacion
calificacion2=int(input("digite su calificacion:"))##El estudiante debe inggresar su segunda calificacion
calificacion3=int(input("digite su calificacion:"))##El estudiante debe ingresar su tercera calificacion
promedio=(calificacion1+calificacion2+calificacion3)/3##Aqui pido que sume las tres calificaciones y divida el resultado en tres
if promedio >=70 : ##mostrar resultados 
    print("el estudiante aprobo") 
else :
    print("el estudiante desaprobo")




