def multiplica_por_2(num):
    lista = []
    for i in range(num + 1):
        lista.append(i * 2)
        return lista
    
def suma_y_resta(lista):
    suma = lista [0] + lista [1]
    print (suma)
    resta = lista [0] - lista [1]
    return resta

def sumatoria_menos_longitud(lista):
    suma = sum (lista)
    longitud = len (lista)
    return suma - longitud

def valores_multiplicados_segundo(lista):
    print(len(lista))

    if len(lista) < 2:
        return[]

segundo = lista[1]
nueva_lista = []
