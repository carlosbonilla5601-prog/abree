print("crear ventanas con una accion")
import tkinter as tk
def mostrar_mensaje():
    ventana_mensaje = tk.Toplevel()
    ventana_mensaje.title("Feliz Cumpleaños")
    ventana_mensaje.geometry("1000x500")
    mensaje = """
FFFFF  EEEEE  L      IIIII  ZZZZZ
F      E      L        I       ZZ
FFFF   EEEE   L        I      ZZ
F      E      L        I     ZZ
F      EEEEE  LLLLL  IIIII  ZZZZZ
 CCCCC  U   U  M   M  PPPP   L      EEEEE    A     Ñ   Ñ   OOO   SSSS
C       U   U  MM MM  P   P  L      E       A A    ÑÑ  Ñ  O   O  S
C       U   U  M M M  PPPP   L      EEEE   AAAAA   Ñ Ñ Ñ  O   O   SSS
C       U   U  M   M  P      L      E      A   A   Ñ  ÑÑ  O   O      S
 CCCCC   UUU   M   M  P      LLLLL  EEEEE  A   A   Ñ   Ñ   OOO   SSSS
"""
    etiqueta = tk.Label(
        ventana_mensaje,
        text=mensaje,
        font=("Consolas", 20),
        justify="left",
        anchor="nw"
    )
    etiqueta.pack(padx=30, pady=30)
ventana = tk.Tk()
ventana.geometry("300x200")
boton = tk.Button(
    ventana,
    text="Mostrar Mensaje",
    command=mostrar_mensaje
)
boton.pack(pady=50)
ventana.mainloop()




