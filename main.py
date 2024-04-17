import matplotlib.pyplot as plt

from UnionFind import UnionFind as UF
from umbralizacion_otsu import umbralizar_otsu_var_clases as otsu
from imagenes import obtener_nombres_imagenes_aleatorias as nombres_img
from imagenes import invertir as inv_img

cant_imgs=2
nombres_imagenes=nombres_img(cant_imgs)
print(nombres_imagenes)

for img in range(cant_imgs):
    #Formar la ruta de la imagen
    ruta_imagen="img/"+nombres_imagenes[img]
    
    #Apliar otsu a la imagen
    img_otsu=otsu(ruta_imagen)

    #Invertir imagen
    imagen=inv_img(img_otsu)

# Ejemplo de uso
n = 6  # Número de elementos
uf = UF(n)

# Unimos algunos conjuntos
uf.union(0, 1)
uf.union(2, 3)
uf.union(4, 5)

# Verificamos la pertenencia a los conjuntos
print(uf.find(0))  # Debería devolver 0, ya que 0 y 1 están en el mismo conjunto
print(uf.find(3))  # Debería devolver 2, ya que 2 y 3 están en el mismo conjunto
print(uf.find(5))  # Debería devolver 4, ya que 4 y 5 están en el mismo conjunto