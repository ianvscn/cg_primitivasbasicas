from tkinter import *
from elipse import Elipse

def onLeftClick(event):
    pixel = (  # Definição do grupo de pixeis
        ("blue")
    )

    print("Event:", event)

    pontosElipse = Elipse.midPointElipse(80, 50, (event.x, event.y))
    for ponto in pontosElipse:
        if((0 <= ponto[0] <= 600) and (0 <= ponto[1] <= 600)):
            imagem.put(pixel, (ponto[0], ponto[1]))

window = Tk()
window.title("Primitivas")
window.resizable(False, False)

#tela
imagem = PhotoImage(width=600,height=600)
tela = Label(window, image=imagem)
tela.bind("<Button-1>", onLeftClick)
tela.pack()

window.mainloop()