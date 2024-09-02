"""
Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se
digitará por teclado. Imprimir el multiplicando, el multiplicador y el producto
"""
## imprimir un saludo al usuario
print("Bienvenido al menú de operaciones matemáticas")
##solicitar al usuario que ingrese el numero del cual se desea la tabla de multiplicar
numero = int(input("introduce el numero para calcular su tabla de multiplicar"))
##Imprimir el encabezado de la tabla 
print(f"/nTabla de multiplicar del {numero}:\n")
print(f"{'multiplicando':>15} {'Multiplicador':<15} {'Producto':<15}")
##utilizar un bucle para generar e imprimir la tabla de multiplicar
for i in range (1,11):
    producto = numero* i
    print(f"{numero} x {i} = {producto}")
    



