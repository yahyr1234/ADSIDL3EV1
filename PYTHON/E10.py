print()
print("=== COSTO DE LLAMADA INTERNACIONAL ===")
print("        AUTOR: NEXUS SISTEMS          ")
print()
# lectura de datos
CODIGO = int(input("INGRESE EL CODIGO DE LA ZONA >>> "))
MINUTOS = int(input("INGRESE LA CANTIDAD DE MINUTOS HABLADOS >>> "))
# validacion
if (MINUTOS > 0):
    # proceso
    if (CODIGO == 10):
        ZONA = "AMERICA DEL NORTE"
        CM = 2.2
    elif (CODIGO == 12):
        ZONA = "AMERICA DEL CENTRO"
        CM = 2.5
    elif (CODIGO == 20):
        ZONA = "AMERICA DEL SUR"
        CM = 1.2
    elif (CODIGO == 22):
        ZONA = "ASIA"
        CM = 3.5
    elif (CODIGO == 30):
        ZONA = "EUROPA"
        CM = 3.0
    elif(CODIGO == 32):
        ZONA = "AFRICA"
        CM = 3.2
    #hallar costo de la llamda
    COSTO=round(CM*MINUTOS, 2)
    #salida de datos 
    print()
    print("LA ZONA GOEGRAFICA ES >> ",ZONA)
    print("EL COSTO POR LA LLAMADA ES >> S/", COSTO )
    print()
else:
    print(">>> ERROR: LOS MINUTOS DEBEN SER MAYORES A 0 <<<")
#fin 