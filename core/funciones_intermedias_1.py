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

#Actualizar valores en diccionarios y listas

#Cambia el valor de 3 en matriz por 6.
matriz[1][0] = 6
print(matriz)

#Cambia el nombre del primer cantante de “Ricky Martin” a “Enrique Martin Morales”
cantantes[0]["nombre"] = "Enrique Martin Morales"
print (cantantes)

#En ciudades, cambia “Cancún” por “Monterrey”
ciudades["México"][2] = "Monterrey"
print(ciudades)

#En las coordenadas, cambia el valor de “latitud” por 9.9355431
coordenadas[0] ["latitud"] = 9.9355431
print(coordenadas)

# 2. Iterar a través de una lista de diccionarios
cantantes = [ 
   {"nombre": "Ricky Martin" , "pais": "Puerto Rico"},
   {"nombre": "Chayanne", "pais": "Puerto Rico"},
   {"nombre": "José José", "pais": "México"},
   {"nombre": "Juan Luis Guerra", "pais": "República Dominicana"} ]

def iterarDiccionario(lista):
    for i in lista:
        pares = []
        for llave, valor in i.items():
            pares.append(f"{llave} - {valor}")
        print(", ".join(pares))

iterarDiccionario(cantantes)


#3. Obtener valores de una lista de diccionarios
def iterarDiccionario2(llave, lista):
    for i in lista:  
        print(i[llave])

iterarDiccionario2("nombre", cantantes) 
iterarDiccionario2("pais", cantantes)


#4. Iterar a través de un diccionario con valores de lista
def imprimirInformacion(diccionario):
    for clave in diccionario:
        lista = diccionario[clave]
        print(len(lista), clave.upper())

        for elemento in lista:
            print(elemento)

        print()
        
costa_rica = {
    "ciudades": ["San Jose", "Limon", "Cartago", "Puntarenas"],
    "comidas":["gallo pinto", "casado", "tamales", "chifrijo", "olla de carne"]
}
imprimirInformacion(costa_rica)