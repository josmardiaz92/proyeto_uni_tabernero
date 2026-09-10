# La Taberna

Aplicación de escritorio en Python donde el usuario conversa con un tabernero medieval. La interfaz está hecha con `tkinter` y el tabernero responderá usando **Google Gemini** como motor de inteligencia artificial.

> **Estado:** en desarrollo. La interfaz gráfica está lista; la integración con Google Gemini está pendiente.

## Contexto académico

- **Universidad:** UPTAIET
- **Materia:** Acreditable II
- **Profesor:** ARCHILA CARDENAS KEVIN JOSEPH

## Autores

- Josmar Diaz
- Andrés Caicedo

## Características

- Ventana con fondo ambientado en una taberna.
- Panel de diálogo del tabernero con scroll personalizado.
- Cuadro de entrada para escribir mensajes.
- Botones para enviar y limpiar el mensaje.
- Atajos de teclado:
  - `Enter`: enviar el mensaje.
  - `Shift + Enter`: salto de línea.

## Requisitos

- Python 3.10 o superior, con `tkinter` incluido.
- Git.
- Dependencias listadas en `requirements.txt` (Pillow).

## Clonar y ejecutar

### Windows (PowerShell)

```powershell
git clone https://github.com/josmardiaz92/proyeto_uni_tabernero.git
cd proyeto_uni_tabernero
python -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
venv\Scripts\python.exe main.py
```

### Linux / macOS

```bash
git clone https://github.com/josmardiaz92/proyeto_uni_tabernero.git
cd proyeto_uni_tabernero
python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
venv/bin/python main.py
```

La carpeta `venv` no se sube al repositorio; cada equipo debe crear la suya con los pasos anteriores.

## Estructura

```
proyeto_uni_tabernero/
├── main.py            # Interfaz y lógica de la aplicación
├── fondo.jpg          # Imagen de fondo
├── requirements.txt   # Dependencias de Python
└── README.md
```

## Problemas conocidos

- **Fuente "Old English Text MT":** viene con Microsoft Office, no con Windows. Si no está instalada, `tkinter` usa otra fuente sin avisar y el panel del tabernero pierde su estilo medieval.
- **Fuente "Georgia":** incluida en Windows y macOS, pero no en la mayoría de distribuciones Linux.
- **`tkinter` en Windows:** es opcional en el instalador de Python. Si aparece `ModuleNotFoundError: No module named 'tkinter'`, reinstala Python marcando la opción "tcl/tk and IDLE".
- **`tkinter` en Linux:** se instala aparte, por ejemplo en Debian/Ubuntu:
  ```bash
  sudo apt install python3-tk
  ```
- **Escalado de pantalla:** la ventana tiene tamaño y posición fijos (960x540). Con escalado de Windows alto (150 % o más) o pantallas pequeñas puede quedar descentrada o cortada.
