#formas de controlar while
"""
idebtificadores o tipos de datos primitivos
por nuemos sea reales o enteros
por booleanos
por cadenas de texto

no primitivos
listas
tuplas
diccionarios
sets
rangos
areglos : vectores, matrices
"""
#region control letra
palabra=input("ingresar palabra: ")
while palabra.lower()=="s":
    palabra=input("ingrese una palabra  nuevo: ")
print("fin del ciclo while")
#endregion
#region control por FALSE o TRUE
contador=0
while True:
    if contador ==10:
        break
        print(contador)
    else:
        print("el contador no ha llegado a 10")
    contador+=1
print("el contador no ha llegado correctanente")
contador+=1
#endregion