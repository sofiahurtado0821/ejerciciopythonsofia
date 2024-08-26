"""Una empresa quiere hacer una compra de varias piezas de la misma clase a una fábrica de bolsos. La empresa, dependiendo del monto total de la compra, decidirá qué hacer para pagar al fabricante:
"""
monto_total = int(input("Ingrese el monto total de la compra: "))


inversion_propia = 0
prestamo_banco = 0
credito_fabricante = 0


if monto_total > 500000:

    inversion_propia = monto_total * 0.55
    prestamo_banco = monto_total * 0.30
    credito_fabricante = monto_total * 0.15
else:

    inversion_propia = monto_total * 0.70
    credito_fabricante = monto_total * 0.30


interes_credito = credito_fabricante * 0.20
total_credito_con_interes = credito_fabricante + interes_credito


print(f"Valor invertido de su propio dinero: ${inversion_propia:,}")
print(f"Valor prestado al banco: ${prestamo_banco:,}")
print(f"Valor del crédito solicitado al fabricante: ${credito_fabricante:,}")
print(f"Intereses sobre el crédito solicitado al fabricante: ${interes_credito:,}")
print(f"Valor total a pagar al fabricante (con intereses): ${total_credito_con_interes:,}")