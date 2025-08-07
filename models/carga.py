import numpy as np

class Carga:
    def __init__(self,x,y,magnitud,masa=1.0,movible=False,principal=False):
        self.x=x
        self.y=y
        self.magnitud=magnitud
        self.masa=masa
        self.movible=movible
        self.principal=principal

    def posicion(self):
        return np.array([self.x,self.y])