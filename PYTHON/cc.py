# Definimos un precio base para cada camisa (puedes cambiar este valor)
PRECIO_CAMISA = 50.00

# 1. Entrada de datos
n = int(input("Ingrese la cantidad de camisas a comprar: "))

# 2. Determinar el porcentaje de descuento usando if-elif-else
if n >= 1 and n <= 4:
    porcentaje_descuento = 12.5
elif n >= 5 and n <= 8:
    porcentaje_descuento = 20.0
elif n > 8:
    porcentaje_descuento = 31.5
else:
    porcentaje_descuento = 0.0  # Por si ingresan 0 o números negativos

# 3. Realizar los cálculos matemáticos básicos
subtotal = n * PRECIO_CAMISA
monto_descuento = subtotal * (porcentaje_descuento / 100)
total_final = subtotal - monto_descuento

# 4. Mostrar los resultados solicitados
print("\n--- RESUMEN DE COMPRA ---")
print(f"Compra final sin descuento: S/ {subtotal:.2f}")
print(f"Monto del descuento ({porcentaje_descuento}%): S/ {monto_descuento:.2f}")
print(f"Compra con descuento (Total a pagar): S/ {total_final:.2f}")
#fin