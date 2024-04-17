"""############################################################
    PRÁCTICA 1.2 - Umbralización de Otsu
        Este programa implementa las características del algo-
        ritmo de umbralización por otsu, se apoya de funciones
        para el cálculo de sumas acumuladas, medias acumuladas,
        varianza entre clases, histograma normalizado, entre -
        otras. El programa devuelve el histograma, de la imagen
        en grises, y en él se muestra el k* óptimo, así como --
        las medias de cada grupo C1 y C2, además se muestra la 
        varianza entre clases, la varianza de cada grupo a par-
        tir de su media y la probabilidad de ocurrencia de cada
        grupo.
   #############################################################"""

#Librerías auxiliares
from PIL import Image
from auxiliares import * #Librería propia de la práctica



"""------------------- FUNCIONES DE UMBRALIZACIÓN -------------------"""

#UMBRALIZACIÓN OTSU, MAXIMIZANDO LA VARIANZA ENTRE CLASES
def umbralizar_otsu_var_clases(ruta_imagen):
    hist_img,cant_px=histograma(ruta_imagen,canal="grises",cant="si")
    histnorm_img=hist_norm(hist_img,cant_px)
    sumacum_img=sum_acum(histnorm_img)
    medacum_img=med_acum(histnorm_img)
    medglobal_img=medacum_img[255]

    #Maximizar la varianza
    sigma_max=0
    suma_k=0
    cant_k=0
    sigma_cuadrada=np.zeros(256,dtype=float)
    for k in range(256):
        sigma_eval=var_clases(medglobal_img,sumacum_img[k],medacum_img[k])
        sigma_cuadrada[k]=sigma_eval
        if sigma_eval>sigma_max:
            sigma_max=sigma_eval
            suma_k=k
            cant_k=1
        elif sigma_eval==sigma_max:
            cant_k+=1
            suma_k+=k

    if cant_k>1:
        k_optimo=suma_k/cant_k
    else:
        k_optimo=suma_k

    #Obtener los mejores 5 k
    n=5
    mejores_cinco = np.argsort(sigma_cuadrada)[-n:][::-1]

    P1=sumacum_img[k_optimo]
    P2=1-P1
    m1,m2=intensidad_med_grupos(k_optimo,medacum_img,P1,histnorm_img)
    #Obtener la varianza de cada grupo
    varianzaC1=0
    varianzaC2=0
    for i in range(k_optimo+1):
        varianzaC1+=(hist_img[i]-m1)**2
    for j in range(k_optimo+1,256):
        varianzaC2+=(hist_img[j]-m2)**2
    varianzaC1/=k_optimo
    varianzaC2/=256-k_optimo
        
    #Imprimir el histrograma
    #plot_histograma_umbral(hist_img,k_optimo,P1,P2,m1,m2,sigma_cuadrada[k_optimo],varianzaC1,varianzaC2)

    #Binarizar imagen
    img_umbralizada=binarizar(ruta_imagen,0,255,99)
    """plt.imshow(img_umbralizada)
    plt.show()"""
    
    return img_umbralizada

#UMBRALIZACIÓN OTSU MAXIMIZANDO LA MEDIA ADIMENSIONAL NORMALIZADA
def umbralizar_otsu_med_adim_norm(ruta_imagen):
    hist_img,cant_px=histograma(ruta_imagen,canal="grises",cant="si")
    histnorm_img=hist_norm(hist_img,cant_px)
    sumacum_img=sum_acum(histnorm_img)
    medacum_img=med_acum(histnorm_img)
    medglobal_img=medacum_img[255]
    var_global_img=var_global(histnorm_img,medglobal_img)

    #Maximizar la medida adimensional normalizada
    eta_max=0
    suma_k=0
    cant_k=0
    eta=np.zeros(256,dtype=float)
    for k in range(256):
        eta_eval=var_clases(medglobal_img,sumacum_img[k],medacum_img[k])/var_global_img
        eta[k]=eta_eval
        if eta_eval>eta_max:
            eta_max=eta_eval
            suma_k=k
            cant_k=1
        elif eta_eval==eta_max:
            cant_k+=1
            suma_k+=k

    if cant_k>1:
        k_optimo=suma_k/cant_k
    else:
        k_optimo=suma_k

    #Obtener los mejores 5 k
    n=5
    mejores_cinco = np.argsort(eta)[-n:][::-1]

    return k_optimo,eta,mejores_cinco


"""---------------- INICIO DEL PROCEDIMIENTO PARA UNA IMAGEN ---------------

#Lectura de imagen
ruta_imagen='img4.jpg' #<-- Cambiar aquí la ruta de la imagen

img=Image.open(ruta_imagen,'r')
mimg=np.array(img)
plt.imshow(mimg,cmap='gray')
plt.show()

#Método de OTSU maximizando la VARIANZA ENTRE CLASES
k_asterisco,varianza_clases,top5=umbralizar_otsu_var_clases(ruta_imagen)
#TOP 5
print("Mejores valores de k =",top5)

#Comparar los resultados obtenidos con el cálculo de la MEDIDA ADIMENSIONAL NORMALIZADA
k_asterisco,medida_adimensional_norm,top5_eta=umbralizar_otsu_med_adim_norm(ruta_imagen)
#TOP 5
print("Mejores valores (COMPROBANDO CON MEDIDA ADIMENSIONAL NORMALIZADA) de k =",top5_eta)

"""