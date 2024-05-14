matriz = [ [10, 15, 20], [3, 7, 14] ]

cantantes = [

   {"nombre": "Ricky Martin", "pais": "Puerto Rico"},

   {"nombre": "Chayanne", "pais": "Puerto Rico"}

]

ciudades = {

   "México": ["Ciudad de México", "Guadalajara", "Cancún"],

   "Chile": ["Santiago", "Concepción", "Viña del Mar"]

}

coordenadas = [

   {"latitud": 8.2588997, "longitud": -84.9399704}

]

matriz[1][0] = 6
cantantes[0]["nombre"] = "Enrique Martin Morales"
ciudades["México"][2] = "Monterrey"
coordenadas[0]["latitud"] = "9.9355431"



#/////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////



#2.IterarDiccionario(cantantes)

def iterarDiccionario(lista):
    for diccionario in lista:
        for llave, valor in diccionario.items():
            print(f"{llave} - {valor}", end=", ")
        print("\n")

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario(cantantes)


#/////////////////////////////////////////////////////////
#/////////////////////////////////////////////////////////


#3.IterarDiccionario2

def iterarDiccionario2(llave, lista):
    for diccionario in lista:
        if llave in diccionario:
            print(diccionario[llave])

cantantes = [
    {"nombre": "Ricky Martin", "pais": "Puerto Rico"},
    {"nombre": "Chayanne", "pais": "Puerto Rico"},
    {"nombre": "José José", "pais": "México"},
    {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"}
]

iterarDiccionario2("nombre", cantantes)


#///////////////////////////////////////////////////////////
#///////////////////////////////////////////////////////////

#4.Iterar a través de un diccionario con valores de lista

def imprimirInformacion(diccionario):
    for clave, valores in diccionario.items():
        print(f"{len(valores)} {clave.upper()}")
        for valor in valores:
            print (valor)
        print()

México = {

   "ciudades": ["Guadalajara", "Cancún", "Puebla", "C.D.M.X"],

   "comidas": ["Tacos", "Burrito", "Enchilladas", "Chiles"]

}

imprimirInformacion(México)