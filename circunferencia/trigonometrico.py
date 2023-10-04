import tkinter as tk
import math

def draw_circle():
    # Configurações iniciais
    canvas.delete("circle")
    radius = int(radius_entry.get())
    center_x = int(center_x_entry.get()) + 200
    center_y = int(center_y_entry.get()) + 200
    centro = [center_x, center_y]
    # Desenha a circunferência usando trigonometria
    pontos = []
    teta = 0

    pixel = (  # Definição do grupo de pixeis
        ("blue")
    )

    while (teta <= 45):
        x = radius * math.cos(teta)
        y = radius * math.sin(teta)

        pontos.extend(pontosDoCirculoPorSimetria(int(x), int(y), centro))
        teta += 1

        for ponto in pontos:
            if((0 <= ponto[0] <= 400) and (0 <= ponto[1] <= 400)):
                canvas.create_line(ponto[0], ponto[1], ponto[0] + 1, ponto[1] +1, fill="blue") 


def pontosDoCirculoPorSimetria(x, y, centro):
        points = []

        points.append((x + centro[0], y + centro[1]))
        points.append((x + centro[0], -y + centro[1]))
        points.append((-x + centro[0], y + centro[1]))
        points.append((-x + centro[0], -y + centro[1]))
        points.append((y + centro[0], x + centro[1]))
        points.append((y + centro[0], -x + centro[1]))
        points.append((-y + centro[0], x + centro[1]))
        points.append((-y + centro[0], -x + centro[1]))

        return points

# Configuração da janela
window = tk.Tk()
window.title("Desenho de Circunferência")
window.geometry("400x400")

# Rótulos e entradas para as configurações da circunferência
radius_label = tk.Label(window, text="Raio:")
radius_label.pack()
radius_entry = tk.Entry(window)
radius_entry.pack()

center_x_label = tk.Label(window, text="Coordenada X do Centro:")
center_x_label.pack()
center_x_entry = tk.Entry(window)
center_x_entry.pack()

center_y_label = tk.Label(window, text="Coordenada Y do Centro:")
center_y_label.pack()
center_y_entry = tk.Entry(window)
center_y_entry.pack()
draw_button = tk.Button(window, text="Desenhar Circunferência", command=draw_circle)
draw_button.pack()

# Canvas para desenhar a circunferência
canvas = tk.Canvas(window, width=400, height=400)
canvas.create_line(0, 200, 400, 200, fill="black")  # Eixo X
canvas.create_line(200, 400, 200, 0, fill="black") #Eixo y
canvas.pack()

window.mainloop()