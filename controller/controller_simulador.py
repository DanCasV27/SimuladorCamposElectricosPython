import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Button, TextBox
from models.carga import Carga
from models.campo_utils import campo_electrico
from views.vista_grafica import dibujar_campo

class Simulador_campo_electrico:
    def __init__(self):
        #aca se crean unas cargas por default.
        self.cargas = [
            Carga(-2, 0, 1e-9, movible=True),
            Carga(2, 0, -1e-9, movible=True),
            Carga(0, 2, 1e-9, movible=True, principal=True),
        ]
        #se inicializan variables para control de cargas
        self.seleccionada=None
        self.dragging=False
        #parametros del espacio simulado 
        self.xmin, self.xmax = -5, 5
        self.ymin, self.ymax = -5, 5
        self.grid_points = 40
        #Configuración de la interfaz gráfica
        self.fig, self.ax = plt.subplots()
        plt.subplots_adjust(bottom=0.25)
        self.fig.canvas.mpl_connect('button_press_event', self.on_press)
        self.fig.canvas.mpl_connect('button_release_event', self.on_release)
        self.fig.canvas.mpl_connect('motion_notify_event', self.on_motion)
        # Botón para agregar una nueva carga
        self.add_ax = plt.axes([0.7, 0.1, 0.1, 0.07])
        self.add_button = Button(self.add_ax, 'Agregar carga')
        self.add_button.on_clicked(self.agregar_carga)
        # Caja de texto para modificar la masa de la carga principal
        self.mass_ax = plt.axes([0.15, 0.1, 0.2, 0.07])
        self.mass_box = TextBox(self.masa_ax, 'Masa principal (kg)', initial=str(self.carga_principal().masa))
        self.mass_box.on_submit(self.cambiar_masa)
        # Caja de texto para modificar la magnitud de la carga principal
        self.q_ax = plt.axes([0.4, 0.1, 0.2, 0.07])
        self.q_box = TextBox(self.maginutd_ax, 'Carga principal (C)', initial=str(self.carga_principal().magnitud))
        self.q_box.on_submit(self.cambiar_magnitud)

        self.update_field()
    # se define funcion para identificar la carga principal
    def carga_principal(self):
        #devuelve la carga principal
        return next(carga for carga in self.cargas if carga.principal)
    def actualizar_campo_electrico(self):
        self.ax.clear()
        x = np.linspace(self.xmin, self.xmax, self.grid_points)
        y = np.linspace(self.ymin, self.ymax, self.grid_points)
        X, Y = np.meshgrid(x, y)
        Ex, Ey = campo_electrico(self.charges, X, Y)
        dibujar_campo(self.ax, X, Y, Ex, Ey, self.charges)
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.ymin, self.ymax)
        self.ax.set_title('Simulador de campo eléctrico')
        self.ax.set_xlabel('x (m)')
        self.ax.set_ylabel('y (m)')
        self.fig.canvas.draw()
    def encontrar_carga_cercana(self,event):
        distancia_minima=float('inf')
        cercana=None
        for carga in self.cargas:
            distancia=np.hypot(event.xdata - carga.x, event.ydata - carga.y)
            if distancia<0.5 and carga.movible:
                if distancia<distancia_minima:
                    distancia_minima=distancia
                    cercana=carga
        return cercana
    #Evento: Detecta el inicio del movimiento de una carga.
    def on_press(self, event):        
        if event.inaxes != self.ax:
            return
        carga = self.encontrar_carga_cercana(event)
        if carga:
            self.seleccionada = carga
            self.dragging = True
    def on_release(self, event):
        self.dragging = False
        self.seleccionada = None
    def on_motion(self, event):
        if not self.dragging or self.seleccionada is None or event.inaxes != self.ax:
            return
        self.seleccionada.x, self.seleccionada.y = event.xdata, event.ydata
        self.actualizar_campo_electrico()
    def agregar_carga(self, event):
        x, y = np.random.uniform(self.xmin, self.xmax), np.random.uniform(self.ymin, self.ymax)
        magnitud = np.random.uniform(-2, 2) * 1e-9
        self.charges.append(Carga(x, y, magnitud, movible=True))
        self.actualizar_campo_electrico()
    def cambiar_masa(self, text):
        try:
            masa = float(text)
            self.carga_principal().masa = masa
            self.actualizar_campo_electrico()
        except ValueError:
            pass
    def cambiar_magnitud(self, text):
        try:
            pmagnitud = float(text)
            self.carga_principal().magnitud = pmagnitud
            self.actualizar_campo_electrico()
        except ValueError:
            pass

    def run(self):
        """
        Inicia la interfaz gráfica del simulador.
        """
        plt.show()
        
    





     
