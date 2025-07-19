import numpy as np
import matplotlib.pyplot as plt

# Constante de Coulomb
k = 8.988e9  # N·m²/C²

# Definimos dos cargas puntuales
cargas = [
    {"pos": np.array([0.3, 0.5]), "q": +1e-6},   # carga positiva (rojo)
    {"pos": np.array([0.7, 0.5]), "q": -1e-6},   # carga negativa (azul)
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

    # Evitamos divisiones por cero (por si coincide un punto con una carga)
    r_squared[r_squared == 0] = 1e-20
    r[r == 0] = 1e-10

    E_magnitude = k * carga["q"] / r_squared
    Ex += E_magnitude * (rx / r)
    Ey += E_magnitude * (ry / r)

# Graficamos el campo con flechas
plt.figure(figsize=(8, 6))
plt.quiver(X, Y, Ex, Ey, color='blue', scale=1e10)

# Dibujamos las cargas con colores y tamaño aumentado
for carga in cargas:
    color = 'red' if carga["q"] > 0 else 'blue'
    plt.plot(carga["pos"][0], carga["pos"][1], 'o', color=color,
             markersize=16, markeredgecolor='white')

# Ajustes finales del gráfico
plt.title("Campo eléctrico de dos cargas")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axis('equal')
plt.grid(True)
plt.tight_layout()
plt.show()
