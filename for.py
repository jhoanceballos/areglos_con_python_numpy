#medicion de ejercision
import time
import os
import sys
inicio=time.time()
for i in range(5):
    print(i)
fin=time.time()
tiempofinal=fin-inicio      
print("time de ejecucion:",tiempofinal)
time.sleep(5) #pausa 5 segundos
if sys.plaform == "win32":
    os.system('cls') #limpia la consola en windows
else:
    os.system('clear')#linpia la consola en unix/linux

#ciclo mientras "ciclo": unknown word.
contador=0    
while contador<=10:
    print(contador)
    contador+=1 #contador = contador +1
"""
    contador = contador +1
    0=0+1
    1=1+1
    2=2+1
    3=3+1
    4=3+1...
"""