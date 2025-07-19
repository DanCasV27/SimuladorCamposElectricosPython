import numpy as np
import matplotlib.pyplot as plt

# Constante de Coulomb
k = 8.988e9  # N·m²/C²

# Definimos dos cargas puntuales
cargas = [
    {"pos": np.array([0.3, 0.5]), "q": +1e-6},   # carga positiva
    {"pos": np.array([0.7, 0.5]), "q": -1e-6},   # carga negativa
]

# Creamos una malla de puntos donde vamos a calcular el campo eléctrico
x = np.linspace(0, 1, 25)
y = np.linspace(0, 1, 25)
X, Y = np.meshgrid(x, y)

# Inicializamos los vectores del campo
Ex = np.zeros(X.shape)
Ey = np.zeros(Y.shape)

# Calculamos el campo eléctrico de cada carga en cada punto
for carga in cargas:
    rx = X - carga["pos"][0]
    ry = Y - carga["pos"][1]
    r_squared = rx**2 + ry**2
    r = np.sqrt(r_squared)
    E_magnitude = k * carga["q"] / r_squared
    Ex += E_magnitude * (rx / r)
    Ey += E_magnitude * (ry / r)

# Graficamos el campo con flechas
plt.quiver(X, Y, Ex, Ey, color='blue', scale=1e10)
plt.title("Campo eléctrico de dos cargas")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axis('equal')
plt.grid(True)
plt.show()
