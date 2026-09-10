import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

from pathlib import Path

BASE = Path(__file__).parent


def mostrar_respuesta(respuesta):
    cuadro_tabernero.configure(state=tk.NORMAL)
    cuadro_tabernero.delete("1.0", tk.END)
    cuadro_tabernero.insert("1.0", respuesta)
    cuadro_tabernero.configure(state=tk.DISABLED)


def enviar_texto(event=None):
    texto = cuadro_texto.get("1.0", tk.END).strip()

    if texto:
        print("Texto enviado:")
        print(texto)
        print("-" * 20)
        limpiar_texto()
    else:
        print("El campo está vacío.")
    return "break"

def limpiar_texto():
    cuadro_texto.delete("1.0", tk.END)

def salto_linea(event=None):
    cuadro_texto.insert(tk.INSERT, "\n")
    return "break"

ventana = tk.Tk()
ventana.title("La Taberna")

ventana.geometry("960x540+290+130")

estilo = ttk.Style()
estilo.theme_use("clam")
estilo.configure(
    "Taberna.Vertical.TScrollbar",
    troughcolor="#C78D5D",
    background="#4B2C18",
    bordercolor="#C78D5D",
    lightcolor="#4B2C18",
    darkcolor="#4B2C18",
    arrowcolor="#C78D5D",
    arrowsize=5,
    gripcount=0
)
estilo.map(
    "Taberna.Vertical.TScrollbar",
    background=[("active","#2B120B"),("pressed", "#2B120B")]
)
estilo.layout("Taberna.Vertical.TScrollbar", [
    ("Vertical.Scrollbar.trough", {
            "sticky": "ns",
            "children": [
                ("Vertical.Scrollbar.thumb", {
                    "sticky": "nswe"
                })
            ]
        })
    ]
)


imagen = Image.open(BASE / "fondo.jpg")
imagen = imagen.resize((960, 540))
imagen_fondo = ImageTk.PhotoImage(imagen)

label_fondo = tk.Label(ventana, image=imagen_fondo)
label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

fuente_medieval = ("Old English Text MT", 14, "bold")
fuente_entrada = ("Georgia", 12, "bold")

panel_tabernero = tk.Frame(
    ventana,
    width=440,
    height=230,
    bg="#8B5A2B",
    highlightbackground="#4B2C18",
    highlightthickness=3,
    bd=0
)
panel_tabernero.place(x=20, y=20)

cuadro_tabernero = tk.Text(
    panel_tabernero,
    height=8,
    width=45,
    wrap=tk.WORD,
    borderwidth=0,
    bg="#C78D5D",
    fg="#2B120B",
    relief="flat",
    padx=16,
    pady=12,
    font=fuente_medieval,
    state=tk.NORMAL,
    cursor="arrow",
    spacing1=4,
    spacing2=4,
    spacing3=4
)
cuadro_tabernero.pack(side="left", fill="both", expand=True)
cuadro_tabernero.insert("1.0", "Bienvenido a mi taberna. ¿En qué os puedo ayudar, noble aventurero?")
cuadro_tabernero.configure(state=tk.DISABLED)

scroll_tabernero = ttk.Scrollbar(
    panel_tabernero,
    orient="vertical",
    command=cuadro_tabernero.yview,
    style="Taberna.Vertical.TScrollbar"
)
scroll_tabernero.pack(side="right", fill="y")
cuadro_tabernero.config(yscrollcommand=scroll_tabernero.set)

cuadro_texto = tk.Text(
    ventana,
    height=4,
    width=33,
    wrap=tk.WORD,
    borderwidth=0,
    bg="#D7A36B",
    fg="#2B120B",
    insertbackground="#2B120B",
    relief="flat",
    padx=14,
    pady=10,
    font=fuente_entrada,
    highlightthickness=2,
    highlightbackground="#7A4A2A",
    highlightcolor="#7A4A2A"
)
cuadro_texto.place(x=20, y=400, relwidth=0.8)
cuadro_texto.bind("<Shift-Return>", salto_linea)
cuadro_texto.bind("<Shift-KP_Enter>", salto_linea)
cuadro_texto.bind("<Return>", enviar_texto)
cuadro_texto.bind("<KP_Enter>", enviar_texto)

boton_enviar = tk.Button(ventana, text="Enviar",bg="#4E3525", command=enviar_texto)
boton_enviar.place(x=20, y=510)

boton_limpiar = tk.Button(ventana, text="Limpiar",bg="#4E3525", command=limpiar_texto)
boton_limpiar.place(x=100, y=510)

ventana.mainloop()