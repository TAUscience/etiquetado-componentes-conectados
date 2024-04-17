from UnionFind import UnionFind as UF




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