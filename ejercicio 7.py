import math
import random

class Punto3D:
    def __init__(self, x=0, y=0, z=0):
        self.__x = x
        self.__y = y
        self.__z = z

    @classmethod
    def from_point(cls, punto):
        return cls(punto.get_x(), punto.get_y(), punto.get_z())

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_z(self):
        return self.__z

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_z(self, z):
        self.__z = z

    def distancia(self, otro_punto):
        return math.sqrt(
            (self.__x - otro_punto.get_x())**2 +
            (self.__y - otro_punto.get_y())**2 +
            (self.__z - otro_punto.get_z())**2
        )

# Crear un arreglo de 10 objetos de tipo Punto3D con valores aleatorios
puntos = [Punto3D(random.uniform(0, 100), random.uniform(0, 100), random.uniform(0, 100)) for _ in range(10)]

# Función para calcular la menor distancia entre todos los puntos
def menor_distancia(puntos):
    min_distancia = float('inf')
    for i in range(len(puntos)):
        for j in range(i + 1, len(puntos)):
            distancia = puntos[i].distancia(puntos[j])
            if distancia < min_distancia:
                min_distancia = distancia
    return min_distancia

# Calcular y mostrar la menor distancia
min_dist = menor_distancia(puntos)
print(f"La menor distancia entre los puntos es: {min_dist}")
