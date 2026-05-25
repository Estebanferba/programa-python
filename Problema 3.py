# --------------------------------------------
# SISTEMA DE AUDITORÍA DE INVENTARIO
# Autor: Esteban Fernandez
# --------------------------------------------

# Función para calcular la cantidad exacta a pedir
def calcular_pedido(stock_actual, stock_minimo):

    if stock_actual < stock_minimo:
        return stock_minimo - stock_actual
    else:
        return 0


# Matriz de artículos
# [Código, Nombre, Stock Actual, Stock Mínimo]

inventario = [
    [101, "Teclado", 5, 10],
    [102, "Mouse", 15, 10],
    [103, "Monitor", 3, 8],
    [104, "Impresora", 7, 7],
    [105, "USB", 2, 12]
]

print("SISTEMA DE AUDITORÍA DE INVENTARIO")
print("--------------------------------------")
print("LISTA DE PEDIDOS")
print("--------------------------------------")

# Recorrer la matriz
for articulo in inventario:

    codigo = articulo[0]
    nombre = articulo[1]
    stock_actual = articulo[2]
    stock_minimo = articulo[3]

    # Llamado a la función
    cantidad_pedir = calcular_pedido(stock_actual, stock_minimo)

    # Mostrar resultado
    print("Artículo:", nombre)
    print("Cantidad exacta a pedir:", cantidad_pedir)
    print("--------------------------------------")