print()
print("===== NUMEROS =====")
print("AUTOR: NEXUS SISTEMS")
print()
#lectura de datos
A=float(input(" INGRESE EL PRIMER NUMERO  >>> "))
B=float(input(" INGRESE EL SEGUNDO NUMERO >>> "))
C=float(input(" INGRESE EL TERCER NUMERO  >>> "))
#proceso 1
if(A>B)and(A>C):
    MAYOR=A
    print(" EL NUMERO MAYOR ES >> ",MAYOR)
elif(B>C):
    MAYOR=B
    print(" EL NUMERO MAYOR ES >> ",MAYOR)
else:
    MAYOR=C
    print(" EL NUMERO MAYOR ES >> ",MAYOR)
#proceso 2
if(A<B)and(A<C):
    MENOR=A
    print(" EL NUMERO MENOR ES >> ",MENOR)
elif(B<C):
    MENOR=B
    print(" EL NUMERO MENOR ES >> ",MENOR)
else:
    MENOR=C
    print(" EL NUMERO MENOR ES >> ",MENOR)
#fin