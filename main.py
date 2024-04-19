import matplotlib.pyplot as plt

from UnionFind import UnionFind as UF
from umbralizacion_otsu import umbralizar_otsu_var_clases as otsu
from imagenes import obtener_nombres_imagenes_aleatorias as nombres_img
from imagenes import invertir as inv_img

from EtiquetadoComponentes import primer_iteracion_componentes_etiquetados_conecta8 as primer_etiquetado_conecta8
from EtiquetadoComponentes import primer_iteracion_componentes_etiquetados_conecta4 as primer_etiquetado_conecta4

from EtiquetadoComponentes import EtiquetadoComponentes_conecta8 as segundo_etiquetado_conecta8
from EtiquetadoComponentes import EtiquetadoComponentes_conecta4 as segundo_etiquetado_conecta4

cant_imgs=1
nombres_imagenes=nombres_img(cant_imgs)
print(nombres_imagenes)


for img in range(cant_imgs):
    #Formar la ruta de la imagen
    ruta_imagen="img/"+nombres_imagenes[img]
    
    #Apliar otsu a la imagen
    img_otsu=otsu(ruta_imagen)

    #Invertir imagen
    imagen=inv_img(img_otsu)


    primera_pasada_conecta8 = primer_etiquetado_conecta8(imagen[:,:,0])

    segunda_pasada_conecta8 = segundo_etiquetado_conecta8(imagen[:,:,0])

    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(primera_pasada_conecta8)
    plt.title('Imagen 1')


    plt.subplot(1, 2, 2)
    plt.imshow(segunda_pasada_conecta8)
    plt.title('Imagen 2')

    plt.tight_layout()
    plt.show()

'''

binarizada_prueba = otsu('prueba.jpg')

etiquetada_prueba = EtiquetadoComponentes(binarizada_prueba[:,:,0])

plt.imshow(etiquetada_prueba)
plt.show()

'''