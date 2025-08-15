# Simulador de Campos Eléctricos en Python

Este simulador visualiza la interacción entre cargas eléctricas y el campo eléctrico generado por ellas, usando la Ley de Coulomb. El proyecto está desarrollado completamente en Python y fue hecho para el proyecto final de fisica 2 para la Ingenieria de Software en Cenfotec.

## Instalación de dependencias

Para ejecutar el simulador, necesitas instalar las siguientes dependencias:

- numpy
- matplotlib

Puedes instalar todas las dependencias ejecutando el siguiente comando en la terminal (desde el directorio raíz del proyecto):

```bash
pip install numpy matplotlib
```

## Ejecución

Para iniciar el simulador, simplemente ejecuta el archivo principal:

```bash
python main.py
```

## Requisitos

- Python 3.7 o superior

## Notas adicionales

- Si tienes problemas con la visualización, asegúrate de que tu entorno tenga soporte para interfaces gráficas (matplotlib).
- Puedes crear un ejecutable (.exe) en Windows usando PyInstaller. Instala PyInstaller con `pip install pyinstaller` y genera el ejecutable con:

```bash
pyinstaller --onefile --windowed main.py
```

## Estructura del proyecto

- `main.py`: Entrada principal del simulador.
- `controller/`: Lógica de control y simulación.
- `models/`: Modelos físicos (cargas, utilidades de campo).
- `views/`: Visualización gráfica.

---

**Importante:**  
Esta lista de dependencias se basa en los archivos detectados por búsqueda de importaciones en el código. Si agregas nuevas funcionalidades o dependencias externas, recuerda actualizar este README.

