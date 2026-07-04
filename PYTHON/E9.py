print()
print("=== COMPRA DE CAMISAS ===")
print("AUTOR: NEXUS SISTEMS")
print()
# lectura de datos
PRECIO = float(input("IGRESE EL PRECIO DE LA CAMISA >>> S/ "))
N = int(input("INGRESE LA CANTIDAD DE CAMISAS >>> "))
# validacion
if (N > 0 and PRECIO > 0):
    # proceso
    CF = round(N * PRECIO, 2)
    if (N >= 1 and N <= 4):                       #descuento de 12.5%
        DESCUENTO = round (CF * 0.125, 2)
    elif (N >= 5 and N <= 8):                     #descuento de 20.0%
        DESCUENTO = round (CF * 0.20, 2)
    else:                                         #descuento de 31.5%
        DESCUENTO = round (CF * 0.315, 2)
    PAGO = round(CF - DESCUENTO, 2)
    #salida de datos 
    print()
    print(" LA COMPRA FINAL SIN DESCUENTO ES >> S/",CF)
    print(" EL MONTO DEL DESCUENTO ES >> S/",DESCUENTO)
    print(" LA COMPRA CON DESCUENTO ES >> S/",PAGO)
    print()
else:
    print(">>> ERROR: LA CANTIDAD DE CAMISAS Y EL PRECIO DEBE SER MAYOR A 0 <<<")
#fin