import matplotlib.pyplot as plt

from UnionFind import UnionFind as UF
from umbralizacion_otsu import umbralizar_otsu_var_clases as otsu
from imagenes import obtener_nombres_imagenes_aleatorias as nombres_img
from imagenes import invertir as inv_img

from EtiquetadoComponentes import primer_iteracion_componentes_etiquetados_conecta8 as primer_etiquetado_conecta8
from EtiquetadoComponentes import primer_iteracion_componentes_etiquetados_conecta4 as primer_etiquetado_conecta4

from EtiquetadoComponentes import EtiquetadoComponentes_conecta8 as segundo_etiquetado_conecta8
from EtiquetadoComponentes import EtiquetadoComponentes_conecta4 as segundo_etiquetado_conecta4

def imprimir_resultados(original,grises,binaria,pasada1,pasada2):

    plt.figure(figsize=(15, 10))

    # Subplots para las dos primeras imágenes arriba
    plt.subplot(3, 2, 1)
    plt.imshow(original)
    plt.title('Imagen original')

    plt.subplot(3, 2, 2)
    plt.imshow(pasada1)
    plt.title('Primer recorrido')    

    # Subplot para la tercera imagen en la segunda fila
    plt.subplot(3, 2, 3)
    plt.imshow(grises)
    plt.title('Imagen en grises')

    # Subplots para las dos últimas imágenes en la tercera fila
    plt.subplot(3, 2, 4)
    plt.imshow(pasada2)
    plt.title('Segundo recorrido')

    plt.subplot(3, 2, 5)
    plt.imshow(binaria)
    plt.title('Imagen binaria')

    # Eliminamos los ejes para una presentación más limpia
    for i in range(1, 6):
        plt.subplot(3, 2, i)
        plt.axis('off')

    plt.tight_layout()
    plt.show()


#Recuperación de imágenes
cant_imgs=3
nombres_imagenes=nombres_img(cant_imgs)

for img in range(cant_imgs):
    #Formar la ruta de la imagen
    ruta_imagen="img/"+nombres_imagenes[img]
    
    #Apliar otsu a la imagen
    img_otsu,img_grises,img_original=otsu(ruta_imagen)

    #Invertir imagen
    imagen=inv_img(img_otsu)

    #Procedimiento para conectividad 8
    primera_pasada_conecta8 = primer_etiquetado_conecta8(imagen[:,:,0])
    segunda_pasada_conecta8 = segundo_etiquetado_conecta8(imagen[:,:,0])

    #Ploteo de resultados conectividad 8
    imprimir_resultados(img_original,img_grises,imagen,primera_pasada_conecta8,segunda_pasada_conecta8)


'''

binarizada_prueba = otsu('prueba.jpg')

etiquetada_prueba = EtiquetadoComponentes(binarizada_prueba[:,:,0])

plt.imshow(etiquetada_prueba)
plt.show()

'''