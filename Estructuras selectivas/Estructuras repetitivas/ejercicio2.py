"""
Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos
números
"""

# Inicializamos la suma en 0
suma = 0

# Repetimos 10 veces para leer 10 números
for i in range(10):
    # Leemos el número negativo
    numero = int(input("Ingrese un número negativo: "))
    
    # Convertimos el número a positivo si es negativo
    if numero < 0:
        numero = -numero
    
    # Sumamos el número positivo
    suma += numero

# Imprimimos la suma total
print("La suma de los números positivos es:",suma)