print()
print("=== TRIANGULO ===")
print("AUTOR: NEXUS SISTEMS")
print()
# lectura de datos
L1 = int(input("INGRESE EL LADO 1 >>> "))
L2 = int(input("INGRESE EL LADO 2 >>> "))
L3 = int(input("INGRESE EL LADO 3 >>> "))
# validacion
if (L1 > 0 and L2 > 0 and L3 > 0):
    #proceso
    if (L1 == L2 and L2 == L3):
        print(">>> ES EQUILATERO <<<")
        PERIMETRO = L1 + L2 + L3
        print("EL PERIMETRO DEL TRIANGULO ES DE:", PERIMETRO , "cm")
    elif (L1 == L2) or (L1 == L3) or (L2 == L3):
        print(">>> ES ISOCELES <<<")
        if (L1 == L2):
            LI=L1,L2
            print("LOS DOS LADOS IGUALES SON:",LI)
        if (L1 == L3):
            LI=L1,L3
            print("LOS DOS LADOS IGUALES SON:",LI)
        if (L2 == L3):
            LI=L2,L3
            print("LOS DOS LADOS IGUALES SON:",LI)
    else:
        print(">>> ES ESCALENO <<<")
        SP = round(L1 + L2 + L3) / 2
        AREA = round((SP* (SP - L1) * (SP - L2) * (SP - L3)) ** 0.5)
        print("EL AREA ES >> ", AREA ,"cm²")
else:
    print("\n>>> ERROR: LOS LADOS DEBEN SER MAYORES A 0 <<<\n")
#fin