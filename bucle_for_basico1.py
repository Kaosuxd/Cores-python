#Basico: Del 0 al 100 

for i in range(0, 101):
    print(i)


#Multiplos de 2  entre 500

for i in range(2, 501, 2):
    print(i)

#contando vanilla ice

for vanillaice in range(1, 101):
    if vanillaice % 10 == 0:
        print("baby")
    elif vanillaice % 5 == 0:
        print("ice ice")    
    else:
        print(vanillaice)

#wow. numero grande a la vista

for i in range(0, 500001, 2):
    print(i)

#Regresame al 3

for i in range(2024, 0, -3):
    print(i)

#Contador dinamico

numInicial = 3
numFinal = 10
multiplo = 2

for i in range(numInicial, numFinal + 1):
    if i % multiplo == 0:
        print(i)