#Importaciones
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def histograma(ruta_img ,canal="todos",cant="no"):
    obj_img = Image.open(ruta_img)
    img=np.array(obj_img)
    alto_img = len(img)
    ancho_img = len(img[0])
    # Arreglo que almacena la frecuencia de cada tono de 0 a 255
    frecuencias = np.zeros(256, dtype=int)
    if(obj_img.mode=="L"):
        for al in range(alto_img):
            for an in range(ancho_img):
                frecuencias[img[al][an]] += 1
        if cant=="si":
            return frecuencias, alto_img*ancho_img
        else:
            return frecuencias
        
    else:
        if canal == "r":
            ch = 0
        elif canal == "g":
            ch = 1
        elif canal == "b":
            ch = 2
        elif canal == "grises":
            ch = 0
            #Transformar la imagen a escala de grises
            img_grises=np.copy(img)
            for al in range(alto_img):
                for an in range(ancho_img):
                    img_grises[al][an] = (img[al][an][0] * 0.21) + (img[al][an][1] * 0.72) + img[al][an][2] * 0.07
            img=img_grises
        else:
            ch = 3
            hrojo, hverde, hazul = np.zeros(256, dtype=int), np.zeros(256, dtype=int), np.zeros(256, dtype=int)

        for al in range(alto_img):
            for an in range(ancho_img):
                if ch == 3:
                    hrojo[img[al][an][0]] += 1
                    hverde[img[al][an][1]] += 1
                    hazul[img[al][an][2]] += 1
                else:
                    frecuencias[img[al][an][ch]] += 1

        if ch == 3:
            if cant=="si":
                return hrojo,hverde,hazul, alto_img*ancho_img
            else:
                return hrojo,hverde,hazul
        else:
            if cant=="si":
                return frecuencias, alto_img*ancho_img
            else:
                return frecuencias


def hist_norm(histograma,cantidad_px):
    hnorm=np.zeros(256, dtype=float)
    for i in range(256):
        hnorm[i]=histograma[i]/cantidad_px

    return hnorm


def sum_acum(histograma_norm):
    acumuladas=np.zeros(256,dtype=float)
    acumuladas[0]=histograma_norm[0]
    for i in range(1,256):
        acumuladas[i]=histograma_norm[i]+acumuladas[i-1]

    return acumuladas


def med_acum(histograma_norm):
    acumuladas=np.zeros(256,dtype=float)
    acumuladas[0]=0
    for i in range(1,256):
        acumuladas[i]=(histograma_norm[i]*i)+acumuladas[i-1]

    return acumuladas


def var_clases(media_global,suma_acumulada,media_acumulada):
    a=(media_global*suma_acumulada-media_acumulada)**2
    if suma_acumulada == 0 or suma_acumulada == 1:
        varianza = -1
    else:
        b = suma_acumulada * (1 - suma_acumulada)
        varianza = a / b
    return varianza


def var_global(histograma_normalizado,media_global):
    varianza=0
    for i in range(256):
        varianza+=((i-media_global)**2)*histograma_normalizado[i]

    return varianza


def binarizar(ruta_img,v1,v2,limite):
    obj_img = Image.open(ruta_img)
    img=np.array(obj_img)
    altura = len(img)
    anchura = len(img[0])
    img_binaria=np.zeros((altura,anchura,3), dtype=int)

    if(obj_img.mode!="L"):
        img_grises=np.zeros((altura,anchura,3), dtype=int)
        for al in range(altura):
            for an in range(anchura):
                img_grises[al][an] = (img[al][an][0] * 0.21) + (img[al][an][1] * 0.72) + img[al][an][2] * 0.07
    
    for al in range(altura):
        for an in range(anchura):
            if(obj_img.mode=="L"):
                if (img[al][an]>=limite):
                    img_binaria[al][an] = v2
                else:
                    img_binaria[al][an] = v1
            else:
                if (img_grises[al][an][0]>=limite):
                    img_binaria[al][an] = v2
                else:
                    img_binaria[al][an] = v1
    
    return img_binaria


def intensidad_med_grupos(umbral,medias_acumuladas,P1,histograma_normalizado):
    m1=medias_acumuladas[umbral]/P1
    m2=0
    for j in range(umbral+1,256):
        m2+=(j*histograma_normalizado[j])
    m2/=1-P1

    return m1,m2


def plot_histograma_umbral(histograma, k, P1, P2, m1, m2, varianza_clases,varianzaC1,varianzaC2):
    # Graficar el histograma
    plt.plot(histograma, color='gray')
    
    # Línea vertical roja en el umbral k
    plt.axvline(x=k, color='red', linestyle='dashed', linewidth=2, label=f'k*={k}')
    
    # Línea vertical anaranjada en m1
    plt.axvline(x=m1, color='orange', linestyle='dashed', linewidth=2, label=f'm1={m1}')
    
    # Línea vertical azul en m2
    plt.axvline(x=m2, color='blue', linestyle='dashed', linewidth=2, label=f'm2={m2}')
    
    # Etiquetas y título
    plt.xlabel('Intensidad')
    plt.ylabel('Frecuencia')
    plt.title('Histograma')
    
    # Etiqueta de leyenda
    plt.legend()
    
    # Anotación de P1, P2, varianza grupo 1, varianza grupo 2
    plt.text(m1, max(histograma), f'P1={P1:.2f}', color='orange', fontsize=7,ha='center')
    plt.text(m1, min(histograma), f'Varianza C1={varianzaC1:.2f}', color='orange', fontsize=7,ha='center')
    plt.text(m2, max(histograma), f'P2={P2:.2f}', color='blue', fontsize=7,ha='center')
    plt.text(m2, min(histograma), f'Varianza C2={varianzaC2:.2f}', color='blue', fontsize=7,ha='center')
    
    # Anotación de varianza entre clases
    plt.text(0, max(histograma), f'Varianza entre clases={varianza_clases:.2f}', color='black', fontsize=7)

    # Mostrar la gráfica
    plt.show()