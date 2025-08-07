# main.py
# Entrada principal del programa: instancia el controlador y ejecuta la simulación.

from controller.controller_simulador import Simulador_campo_electrico

if __name__ == "__main__":
    # Crea el simulador y lo ejecuta
    sim = Simulador_campo_electrico()
    sim.run()