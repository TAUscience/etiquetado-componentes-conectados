class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]  # Inicialmente, cada elemento es su propio padre
        self.rank = [0] * n  # Inicialmente, todas las alturas de los árboles son 0

    def find(self, x):
        if self.parent[x] != x:
            # Si el elemento no apunta directamente a su padre, lo buscamos recursivamente
            self.parent[x] = self.find(self.parent[x])  # Compresión de camino
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        # Si los elementos ya están en el mismo conjunto, no hacemos nada
        if root_x == root_y:
            return

        # Unimos los conjuntos ajustando el padre del conjunto más pequeño al del más grande
        if self.rank[root_x] < self.rank[root_y]:
            self.parent[root_x] = root_y
        elif self.rank[root_x] > self.rank[root_y]:
            self.parent[root_y] = root_x
        else:
            # Si ambos tienen la misma altura, elegimos uno para ser el padre y aumentamos su altura
            self.parent[root_y] = root_x
            self.rank[root_x] += 1