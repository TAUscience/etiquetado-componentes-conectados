#Librerías auxiliares
from PIL import Image
from auxiliares import * #Librería propia de la práctica

"""------------------- FUNCIONES DE UMBRALIZACIÓN -------------------"""

#UMBRALIZACIÓN OTSU, MAXIMIZANDO LA VARIANZA ENTRE CLASES
def umbralizar_otsu_var_clases(ruta_imagen):
    hist_img,cant_px,img_grises,img_original=histograma(ruta_imagen,canal="grises",cant="si")
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

    #Binarizar imagen
    img_umbralizada=binarizar(ruta_imagen,0,255,k_optimo)
    
    return img_umbralizada, img_grises, img_original