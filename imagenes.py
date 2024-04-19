import random

def obtener_nombres_imagenes_aleatorias(n):
    numeros_img=random.sample(range(100, 169 + 1), n)
    nombres_img=[]
    for numero in numeros_img:
        numero_cadena=str(numero)
        nombres_img.append("cropped_parking_lot_"+numero_cadena+".JPG")

    return nombres_img

def invertir(img):
    # Crear una copia de la imagen binaria invertida
    imagen_invertida = img.copy()
    # Invertir los valores de los píxeles
    imagen_invertida[img == 255] = 0
    imagen_invertida[img == 0] = 255
    return imagen_invertida
