import matplotlib.pyplot as plt
def dibujar_campo(eje_dibujo,X,Y,Ex,Ey,cargas):
    magnitud_campo=(Ex**2 + Ey**2)**0.5
    eje_dibujo.streamplot(X, Y, Ex, Ey, color=magnitud_campo, linewidth=1, cmap='cool', density=1.2) # esta linea lo que hace es dibujar las cargas como circulos
    for carga in cargas:
        color='red' if carga.magnitud>0 else 'blue'
        if getattr(carga,'principal',False):
            color='green'
        eje_dibujo.plot(carga.x, carga.y, 'o', color=color, markersize=15)
        eje_dibujo.text(carga.x, carga.y, f'{carga.q:.1e}C\n{carga.masa:.1f}kg', color='black',
                ha='center', va='center', fontsize=7)

