import numpy as np
from UnionFind import UnionFind as UF
import random
import matplotlib.pyplot as plt


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

    etiquetas_equivalentes = generar_tuplas_equivalentes(elementos)

    etiqueta_maxima = max(elementos)

    if(etiqueta_maxima == 0):
        etiqueta_actual = etiqueta_global
        etiqueta_global+=1
    else:
        etiqueta_minima = min(x for x in elementos if x != 0)
        etiqueta_actual = etiqueta_minima

        if(etiquetas_equivalentes):
            print(f"Componente: {etiqueta_actual}")
            print('Componentes Hijos:')
            print(etiquetas_equivalentes)

    return etiqueta_actual, etiqueta_global, etiquetas_equivalentes

def conecta_4(seccion,y,x,etiqueta_global):
    elementos = []
    elementos.append(seccion[y-1][x])
    elementos.append(seccion[y][x-1]) 

    etiquetas_equivalentes = generar_tuplas_equivalentes(elementos)

    etiqueta_maxima = max(elementos)

    if(etiqueta_maxima == 0):
        etiqueta_actual = etiqueta_global
        etiqueta_global+=1
    else:
        etiqueta_minima = min(x for x in elementos if x != 0)
        etiqueta_actual = etiqueta_minima

        if(etiquetas_equivalentes):
            print(f"Componente: {etiqueta_actual}")
            print('Componentes Hijos:')
            print(etiquetas_equivalentes)

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

    return imagen_con_margen, etiquetas_equivalentes, etiqueta_global

def generar_etiquetado_conecta8(imagen):
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

    return imagen_con_margen, etiquetas_equivalentes, etiqueta_global

def generar_etiquetado_conecta4(imagen):
    imagen_con_margen = crear_margen_ceros(imagen)
    filas, columnas = imagen_con_margen.shape
    
    etiqueta_global = 1
    etiquetas_equivalentes = []

    for i in range(1,filas-1):
        for j in range(1,columnas-1):

            if(imagen_con_margen[i][j] != 0):

                datos = conecta_4(imagen_con_margen,i,j,etiqueta_global)
                
                imagen_con_margen[i][j] = datos[0]
                etiqueta_global = datos[1]
                
                for k in datos[2]:
                    if (k not in etiquetas_equivalentes):
                        etiquetas_equivalentes.append(k)

    return imagen_con_margen, etiquetas_equivalentes, etiqueta_global

def etiquetar_usando_UnionFind(imagen_etiquetada, tuplas_equivalentes, etiqueta_max1):
    filas, columnas = imagen_etiquetada.shape

    imagen = np.zeros((filas - 2, columnas - 2), dtype=imagen_etiquetada.dtype)
    imagen = imagen_etiquetada[1:-1, 1:-1]

    #n = max([tupla[1] for tupla in tuplas_equivalentes])
    uf = UF(etiqueta_max1)

    if tuplas_equivalentes:
        for tupla in tuplas_equivalentes:
            uf.union(tupla[0],tupla[1])

    for i in range(filas - 2):
        for j in range(columnas - 2):
            if(imagen[i][j] != 0):
                if uf.find(imagen[i][j]):
                    imagen[i][j] = uf.find(imagen[i][j])


    return imagen

def colorear_componentes_etiquetados(imagen_etiquetada):
    filas, columnas = imagen_etiquetada.shape
    imagen_RGB = np.zeros((filas, columnas, 3), dtype=np.uint8)

    etiqueta_global = 0
    etiquetas_enumeradas = []
    colores_RGB = []

    for i in range(filas):
        for j in range(columnas):
            if(imagen_etiquetada[i][j] != 0 and imagen_etiquetada[i][j] not in etiquetas_enumeradas):
                etiquetas_enumeradas.append(imagen_etiquetada[i][j])
                R = random.randint(60, 255)
                G = random.randint(60, 255)
                B = random.randint(60, 255)
                colores_RGB.append((R,G,B))

            if(imagen_etiquetada[i][j]):
                posicion = etiquetas_enumeradas.index(imagen_etiquetada[i][j])
                RGB = colores_RGB[posicion]

                imagen_RGB[i][j][0] = RGB[0]
                imagen_RGB[i][j][1] = RGB[1]
                imagen_RGB[i][j][2] = RGB[2]

    return imagen_RGB

def EtiquetadoComponentes(imagen_binaria):
    matriz_etiquetada = generar_etiquetado(imagen_binaria)

    componentes_unidos = etiquetar_usando_UnionFind(matriz_etiquetada[0],matriz_etiquetada[1],matriz_etiquetada[2])

    imagen_coloreada = colorear_componentes_etiquetados(componentes_unidos)

    return imagen_coloreada

def EtiquetadoComponentes_conecta8(imagen_binaria):
    matriz_etiquetada = generar_etiquetado_conecta8(imagen_binaria)

    componentes_unidos = etiquetar_usando_UnionFind(matriz_etiquetada[0],matriz_etiquetada[1],matriz_etiquetada[2])

    imagen_coloreada = colorear_componentes_etiquetados(componentes_unidos)

    return imagen_coloreada

def EtiquetadoComponentes_conecta4(imagen_binaria):
    matriz_etiquetada = generar_etiquetado_conecta4(imagen_binaria)

    componentes_unidos = etiquetar_usando_UnionFind(matriz_etiquetada[0],matriz_etiquetada[1],matriz_etiquetada[2])

    imagen_coloreada = colorear_componentes_etiquetados(componentes_unidos)

    return imagen_coloreada

def primer_iteracion_componentes_etiquetados(imagen_binaria):
    matriz_etiquetada = generar_etiquetado(imagen_binaria)
    imagen_coloreada = colorear_componentes_etiquetados(matriz_etiquetada[0])

    return imagen_coloreada

def primer_iteracion_componentes_etiquetados_conecta8(imagen_binaria):
    matriz_etiquetada = generar_etiquetado_conecta8(imagen_binaria)
    imagen_coloreada = colorear_componentes_etiquetados(matriz_etiquetada[0])

    return imagen_coloreada

def primer_iteracion_componentes_etiquetados_conecta4(imagen_binaria):
    matriz_etiquetada = generar_etiquetado_conecta4(imagen_binaria)
    imagen_coloreada = colorear_componentes_etiquetados(matriz_etiquetada[0])

    return imagen_coloreada


'''

matriz = np.array([[1, 0, 0, 0, 0, 1, 0],
                   [0, 0, 0, 1, 1, 0, 0],
                   [0, 1, 0, 0, 1, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [1, 0, 0, 1, 0, 1, 0],
                   [0, 0, 0, 0, 0, 0, 0],
                   [1, 1, 1, 0, 1, 0, 1]])


imagen_etiquetada = EtiquetadoComponentes(matriz)

plt.imshow(imagen_etiquetada)
plt.show()


'''