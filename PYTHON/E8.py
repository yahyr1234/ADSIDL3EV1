print()
print("=== ORDENAR TRES NUMEROS ===")
print("AUTOR: NEXUS SISTEMS")
print()
# lectura de datos
A = int(input("INGRESE EL NUMERO 1 >>> "))
B = int(input("INGRESE EL NUMERO 2 >>> "))
C = int(input("INGRESE EL NUMERO 3 >>> "))
print()
print("1. ASCENDENTE (MENOR A MAYOR)")
print("2. DESCENDENTE (MAYOR A MENOR)")
print()
OPCION = input("ELIJA UNA OPCION >>> ")
print()
# validacion
if (A != B and A != C and B != C): 
    # proceso
    MENOR = A
    if (B < MENOR):
        MENOR = B
    if (C < MENOR):
        MENOR = C
    MAYOR = A
    if (B > MAYOR):
        MAYOR = B
    if (C > MAYOR):
        MAYOR = C
    #hallar medio
    MEDIO = (A + B + C) - MENOR - MAYOR
    ASCENDENTE=(MENOR,MEDIO,MAYOR)
    DESCENDENTE=(MAYOR,MEDIO,MENOR)
    #salida de datos
    if (OPCION == "1"):
        print(" >>> ORDEN ASCENDENTE <<< ")
        print(ASCENDENTE)
    elif (OPCION == "2"):
        print(" >>> ORDEN DESCENDENTE <<< ")
        print(DESCENDENTE)
else:
    print(">>> ERROR: LOS NUMEROS DEBEN SER DIFERENTES <<<")
#fin 