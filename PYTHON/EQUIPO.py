print()
print("======")
print("AUTOR:")
print()
#leer datos
CANT=int(input("INGRESE LA CANTIDAD DE LLANTAS:"))
PRECIO=int(input("INGRESE EL PRECIO:"))
#proceso 
if (CANT<5):
    PRECIO=150
else:
    PRECIO=120
TOTAL=round(CANT*PRECIO)
#salida
print("EL TOTAL ES:S/",TOTAL,)
#fin 