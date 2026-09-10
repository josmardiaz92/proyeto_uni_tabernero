# La Taberna

Aplicación de escritorio en Python donde el usuario conversa con Bartolo, un tabernero medieval. La interfaz está hecha con `tkinter`, las respuestas las genera **Google Gemini** y el tabernero las lee en voz alta con `pyttsx3`.

## Contexto académico

- **Universidad:** UPTAIET
- **Materia:** Acreditable II
- **Profesor:** ARCHILA CARDENAS KEVIN JOSEPH

## Autores

- Josmar Diaz
- Andrés Caicedo

## Características

- Conversación con el tabernero usando Google Gemini (modelo `gemini-3.6-flash`), manteniendo el historial del chat durante la sesión.
- El tabernero no rompe el personaje: responde en español antiguo, en 3 o 4 frases.
- Lectura en voz alta de cada respuesta (texto a voz sin conexión, con las voces del sistema).
- La consulta a la IA corre en un hilo aparte, así la ventana no se congela mientras espera.
- Ventana con fondo ambientado en una taberna e icono propio.
- Panel de diálogo del tabernero con scroll personalizado.
- Cuadro de entrada para escribir mensajes, con botones para enviar y limpiar.
- Diálogo de confirmación al cerrar la ventana.
- Atajos de teclado:
  - `Enter`: enviar el mensaje.
  - `Shift + Enter`: salto de línea.
  - `Escape`: salir (pide confirmación).

## Requisitos

- Python 3.10 o superior, con `tkinter` incluido (probado con Python 3.14).
- Git.
- Una clave de API de Google Gemini, que se obtiene gratis en [Google AI Studio](https://aistudio.google.com/apikey).
- Dependencias listadas en `requirements.txt`. Las principales son:
  - `google-genai`: cliente de Google Gemini.
  - `python-dotenv`: carga la clave desde el archivo `.env`.
  - `pillow`: carga y escala la imagen de fondo.
  - `pyttsx3`: texto a voz.

  En Windows también se instalan `pywin32`, `pypiwin32` y `comtypes`, que `pyttsx3` necesita para usar las voces del sistema. En Linux y macOS se omiten solos.

## Clonar y ejecutar

### Windows (PowerShell)

```powershell
git clone https://github.com/josmardiaz92/proyeto_uni_tabernero.git
cd proyeto_uni_tabernero
python -m venv venv
venv\Scripts\python.exe -m pip install -r requirements.txt
Copy-Item .env.example .env
venv\Scripts\python.exe main.py
```

### Linux / macOS

```bash
git clone https://github.com/josmardiaz92/proyeto_uni_tabernero.git
cd proyeto_uni_tabernero
python3 -m venv venv
venv/bin/python -m pip install -r requirements.txt
cp .env.example .env
venv/bin/python main.py
```

Antes de ejecutar `main.py`, abre `.env` y reemplaza `aqui_va_la_clave` con tu clave:

```
GEMINI_API_KEY=tu_clave_de_gemini
```

Si falta la clave, el programa se cierra con el mensaje `Falta GEMINI_API_KEY en el archivo .env`.

Las carpetas `venv` y el archivo `.env` no se suben al repositorio; cada equipo debe crear los suyos con los pasos anteriores. No compartas tu clave de API.

## Estructura

```
proyeto_uni_tabernero/
├── main.py            # Interfaz, conexión con Gemini y texto a voz
├── fondo.jpg          # Imagen de fondo
├── icono.png          # Icono de la ventana
├── requirements.txt   # Dependencias de Python
├── .env.example        # Plantilla del archivo .env
├── .gitignore
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
- **Voz en Linux:** `pyttsx3` necesita `espeak-ng`, por ejemplo en Debian/Ubuntu:
  ```bash
  sudo apt install espeak-ng
  ```
- **Acento de la voz:** `pyttsx3` usa la voz predeterminada del sistema. Si no hay una voz en español instalada, el tabernero lee el texto con acento inglés.
- **Botón "Enviar" bloqueado durante la voz:** el botón se reactiva cuando el tabernero termina de hablar, no cuando aparece la respuesta.
- **Errores de la API:** si la clave es inválida, se agota la cuota o no hay internet, el error aparece en el panel del tabernero (por ejemplo `(Error 429: ...)`).
- **Escalado de pantalla:** la ventana tiene tamaño y posición fijos (960x540). Con escalado de Windows alto (150 % o más) o pantallas pequeñas puede quedar descentrada o cortada.
