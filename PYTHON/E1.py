print()
print("===== LLANTERIA =====")
print(" AUTOR: NEXUS SISTEMS")
print()
#lectura de datos
CANT=int(input(" INGRESE EL NUMERO DE LLANTAS QUE DESEA COMPRAR >> "))
#validacion:
if(CANT>0):
    #proceso
    if(CANT>=5):
        PRECIO = 120
        TOTAL= round((CANT*120),2)
        print(" EL TOTAL A PAGAR ES >> S/",TOTAL)
    else:
        PRECIO = 150
        TOTAL=round((CANT*150),2)
        print(" EL TOTAL A PAGAR ES >> S/",TOTAL)
else:
    print("\n >>> ERROR: AL INGRESAR EL NUMERO DE LLANTAS QUE USTED DESEA COMPRAR <<< \n")
#fin