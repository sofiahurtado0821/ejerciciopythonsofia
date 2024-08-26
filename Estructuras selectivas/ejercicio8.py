"""
Tomando como base los resultados obtenidos en un laboratorio de análisis clínicos, un médico determina si una persona tiene anemia o no, lo cual depende de su nivel 
de hemoglobina en la sangre, de su edad y de su sexo. Si el nivel de hemoglobina que tiene una persona es menor que el rango que le corresponde, se determina su 
resultado como positivo y en caso contrario como negativo. 
"""
edad = int(input("Ingrese la edad: "))
sexo = input("Ingrese el sexo (M/F): ")
nivel_hemoglobina = int(input("Ingrese el nivel de hemoglobina: "))


if edad <= 1/12:  
    rangoMin, rangoMax = 13, 26
elif edad <= 6/12:  
    rangoMin, rangoMax = 10, 18
elif edad <= 12/12:  
    rangoMin, rangoMax = 11, 15
elif edad <= 5:  
    rangoMin, rangoMax = 11.5, 15
elif edad <= 10:  
    rangoMin, rangoMax = 12.6, 15.5
elif edad <= 15:  
    rangoMin, rangoMax = 13, 15.5
else:  
    if sexo == 'F':
        rangoMin, rangoMax = 12, 16
    elif sexo == 'M':
        rangoMin, rangoMax = 14, 18
    else:
        print("Sexo no válido.")
        exit()
if rangoMin <= nivel_hemoglobina <= rangoMax:
    resultado = "negativo"  
else:
    resultado = "positivo" 

print(f"El resultado es: {resultado}")