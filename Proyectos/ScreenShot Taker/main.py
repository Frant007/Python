import tkinter as tk
import pyautogui
import tkinter.filedialog as fd

# Creamos la funcion que nos permite tomar la screenshot
def take_screenshot():
    ask_save = fd.askdirectory() # Preguntamos donde quiere guardar la captura
    if ask_save:
        if not ask_save.endswith(".png"):
            ask_save += ".png"
        captura = pyautogui.screenshot()
        captura.save(ask_save)

# Creamos la ventana y el botón
root = tk.Tk()
root.geometry("300x100")
root.title("Screenshot Taker")
button = tk.Button(root, text="Tomar captura", command=take_screenshot)
button.pack()
root.mainloop()
