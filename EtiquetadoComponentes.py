import numpy as np

def generar_tuplas_equivalentes(lista):
    tuplas = []
    numero_anterior = None
    for numero in lista:
        if numero != 0:
            if numero_anterior is not None and numero != numero_anterior:
                nueva_tupla = (numero_anterior, numero)
                tupla_inversa = (numero, numero_anterior)
                if nueva_tupla not in tuplas and tupla_inversa not in tuplas:
                    tuplas.append(nueva_tupla)
            numero_anterior = numero
    return tuplas


def conecta_8(seccion,y,x,etiqueta_global):
    elementos = []
    elementos.append(seccion[y-1][x+1]) 
    elementos.append(seccion[y-1][x]) 
    elementos.append(seccion[y-1][x-1]) 
    elementos.append(seccion[y][x-1]) 

    etiqueta_minima = min(elementos)
    etiqueta_maxima = max(elementos)

    if(etiqueta_maxima == 0):
        etiqueta_actual = etiqueta_global
        etiqueta_global+=1
    else:
        etiqueta_minima = min(x for x in elementos if x != 0)
        etiqueta_actual = etiqueta_minima
    

    etiquetas_equivalentes = generar_tuplas_equivalentes(elementos)

    return etiqueta_actual, etiqueta_global, etiquetas_equivalentes


def crear_margen_ceros(imagen):
    filas, columnas = imagen.shape
    imagen_con_margenes = np.zeros((filas + 2, columnas + 2), dtype=imagen.dtype)
    imagen_con_margenes[1:-1, 1:-1] = imagen
    
    return imagen_con_margenes



def generar_etiquetado(imagen):

    imagen_con_margen = crear_margen_ceros(imagen)
    filas, columnas = imagen_con_margen.shape
    
    etiqueta_global = 1
    etiquetas_equivalentes = []

    for i in range(1,filas-1):
        for j in range(1,columnas-1):

            if(imagen_con_margen[i][j] != 0):

                datos = conecta_8(imagen_con_margen,i,j,etiqueta_global)
                
                imagen_con_margen[i][j] = datos[0]
                etiqueta_global = datos[1]
                
                for k in datos[2]:
                    if (k not in etiquetas_equivalentes):
                        etiquetas_equivalentes.append(k)


    return imagen_con_margen, etiquetas_equivalentes


matriz = np.array([[1, 0, 0, 0, 1],
                   [1, 0, 0, 1, 0],
                   [0, 0, 1, 0, 0],
                   [1, 1, 0, 0, 0],
                   [1, 1, 0, 1, 1]])


matriz_etiquetada = generar_etiquetado(matriz)


print(matriz_etiquetada[0])
print('......')
print(matriz_etiquetada[1])
