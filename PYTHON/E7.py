print()
print("=== PAGO DE LLAMADA ===")
print("AUTOR: NEXUS SISTEMS")
print()
# lectura de datos
MINUTOS = int(input("INGRESE LA DURACION DE LA LLAMADA (MIN) >>> "))
DOMINGO = input("¿ES DOMINGO? (SI/NO) >>> ").upper()
NOCTURNO = input("¿ES TURNO NOCTURNO? (SI/NO) >>> ").upper()
# validacion
if (MINUTOS > 0) and (DOMINGO == "SI" or DOMINGO == "NO") and (NOCTURNO == "SI" or NOCTURNO == "NO"):
    # proceso
    if (MINUTOS <= 5):
        PRECIO = round(MINUTOS * 1.00, 2)
    elif (MINUTOS <= 8):
        PRECIO = round ((5 * 1.00) + ((MINUTOS - 5) * 0.80), 2)
    elif (MINUTOS <= 10):
        PRECIO = round ((5 * 1.00) + (3 * 0.80) + ((MINUTOS - 8) * 0.70), 2)
    else:
        PRECIO = round ((5 * 1.00) + (3 * 0.80) + (2 * 0.70) + ((MINUTOS - 10) * 0.50), 2)
    #proceso si es dia domingo 
    if (DOMINGO == "SI"):        
        if (NOCTURNO == "SI"):
            IMPUESTO = round(PRECIO * 0.05, 2)
        else:
            IMPUESTO = round(PRECIO * 0.03, 2)
    else:
        IMPUESTO = 0
    TOTAL = round(PRECIO + IMPUESTO, 2)
    #salida de datos 
    print()
    print(">>> DETALLE DE PAGO POR CADA CONCEPTO <<<")
    print()
    print("PRECIO BASE ES   >> S/", PRECIO)
    print("IMPUESTO ES      >> S/", IMPUESTO)
    print("TOTAL A PAGAR ES >> S/", TOTAL)
    print()

else:
    print(">>> ERROR: DATOS NO VALIDOS !!! <<<")
#fin
