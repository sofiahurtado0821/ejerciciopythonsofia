"""
Calcular el número de pulsaciones que debe tener una persona por cada 10 segundos de ejercicio
aeróbico; la fórmula que se aplica es:
cuando el sexo es femenino: núm. pulsaciones = (220 - edad)/10
y si el sexo es masculino: núm. pulsaciones = (210 - edad)/10
"""
sexo=input("ingrese su sexo(femenino, masculino):")
edad=int(input("ingrese su edad:"))
if sexo == "femenino" :
    pulsaciones=(220-edad)/10
else :
    pulsaciones=(210-edad)/10
print(f"el  numero de pulsaciones por cada 10 segundos de ejercicio es:{pulsaciones}")