#Crea una lista de diccionarios llamada ventas, donde cada diccionario represente una venta.
ventas = [
    {"fecha": "2024-01-10", "producto": "Mouse", "cantidad": 3, "precio" : 20.0},
    {"fecha" : "2024-01-10","producto":"Teclado", "cantidad": 1, "precio" : 40.0},
    {"fecha": "2024-01-11", "producto":"Mouse", "cantidad" : 2, "precio": 20.0},
    {"fecha" : "2024-01-12", "producto": "Auriculares", "cantidad": 2, "precio": 30.0}
]

#Utiliza un bucle para iterar sobre la lista ventas y calcular los ingresos totales generados por todas las ventas. 
#Los ingresos totales se calculan multiplicando la cantidad vendida por el precio unitario para cada venta y sumando los resultados.

ingresos_totales = 0
for i in ventas: 
    ingresos_totales += i["cantidad"] * i["precio"]

print(ingresos_totales)

#Crea un diccionario llamado ventas_por_producto donde las claves sean los nombres de los productos y los valores sean la cantidad total vendida de cada producto.
#Utiliza este diccionario para identificar el producto que tuvo la mayor cantidad total vendida.

ventas_por_producto = {}
for i in ventas:
    producto = i["producto"]
    cantidad = i["cantidad"]

    if producto in ventas_por_producto:
        ventas_por_producto [producto] += cantidad
    else:
        ventas_por_producto[producto] = cantidad

print(ventas_por_producto)

producto_mas_vendido = max(ventas_por_producto, key=ventas_por_producto.get)
print(producto_mas_vendido)
print(ventas_por_producto[producto_mas_vendido])


#Crea un diccionario llamado precios_por_producto donde las claves sean los nombres de los productos y los valores sean tuplas. Cada tupla debe contener dos elementos: la suma de los precios de venta de todas las unidades vendidas y la cantidad total de unidades vendidas.

precios_por_producto ={}

for i in ventas: 
    producto = i["producto"]
    cantidad = i["cantidad"]
    precio = i["precio"]

    if producto in precios_por_producto:
        suma, cantidad_total= precios_por_producto[producto]
        precios_por_producto[producto] = (suma + precio * cantidad, cantidad_total + cantidad)
    else:
        precios_por_producto[producto]= (precio * cantidad, cantidad)

#Calcula el precio promedio de venta para cada producto utilizando la información de este diccionario.
for producto in precios_por_producto:
    suma, cantidad_total = precios_por_producto[producto]
    promedio = suma / cantidad_total
    print(producto, promedio)

#Crea un diccionario llamado ingresos_por_dia donde las claves sean las fechas y los valores sean los ingresos totales generados en cada día.
#Utiliza un bucle para calcular los ingresos totales por día y almacenar estos valores en el diccionario.

ingresos_por_dia = {}

for i in ventas:
    fecha = i["fecha"]
    ingreso= i["cantidad"] * i["precio"]

    if fecha in ingresos_por_dia:
        ingresos_por_dia[fecha] += ingreso
    else:
        ingresos_por_dia[fecha] = ingreso

print(ingresos_por_dia)

#Crea un diccionario llamado resumen_ventas donde las claves sean los nombres de los productos y los valores sean diccionarios anidados.

resumen_ventas = {}

for producto in ventas_por_producto:
    cantidad_total = ventas_por_producto[producto]

    ingresos = 0
    for venta in ventas:
        if venta["producto"] == producto:
            ingresos += venta["cantidad"] * venta["precio"]

     #promedio
    suma, cantidad_total_precio = precios_por_producto[producto]
    promedio = suma / cantidad_total_precio
    
    resumen_ventas[producto] = {
        "cantidad_total": cantidad_total,
        "ingresos_totales": ingresos,
        "precio_promedio": promedio
}
    
print(resumen_ventas)