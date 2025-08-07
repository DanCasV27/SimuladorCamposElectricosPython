import numpy as np
from constantes import K 

def campo_electrico(cargas, X , Y):
    """
    Calcula el campo eléctrico en todos los puntos del grid generado por las cargas.

    Args:
        charges (list of Charge): Lista de objetos Charge.
        X (ndarray): Matriz de coordenadas x (meshgrid).
        Y (ndarray): Matriz de coordenadas y (meshgrid).

    Returns:
        Ex, Ey (ndarray): Componentes del campo eléctrico en cada punto del grid.
    """
    Ex,Ey=np.zeros(X.shape), np.zeros(Y.shape)
    for carga in cargas:
        dx= X-carga.x #aca estamos generando las cargas para la formula de la ley de coulumb
        dy=Y-carga.y #aca estamos generando las cargas para la formula de la ley de coulumb
        r2=dx**2+dy**2 #aca generamos r2 que es la distancia desde la carga al punto donde calculamos el campo
        r2[r2==0]=np.nan
        #ahora aplicamos la ley de coulumb
        Ex+= K*carga.magnitud * dx/(r2*np.sqrt(r2))
        Ey+= K*carga.magnitud * dy/(r2*np.sqrt(r2))
    return Ex, Ey