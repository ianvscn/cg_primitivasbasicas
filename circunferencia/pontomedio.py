import tkinter as tk
import math

def draw_circle():
    # Configurações iniciais
    canvas.delete("circle")
    radius = int(radius_entry.get())
    center_x = int(center_x_entry.get())
    center_y = int(center_y_entry.get())

    # Inicializa as coordenadas iniciais
    x = radius
    y = 0
    d = 1 - radius  # Valor inicial de d

    # Desenha a circunferência usando o algoritmo do ponto médio
    while x >= y:
        plot_circle_points(center_x, center_y, x, y)
        y += 1

        # Verifica se a decisão deve ser mudada
        if d <= 0:
            d = d + 2 * y + 1
        else:
            x -= 1
            d = d + 2 * (y - x) + 1

    # Calcula as coordenadas dos pontos mais altos e mais baixos
    highest_point = (center_x, center_y - radius)
    lowest_point = (center_x, center_y + radius)

    # Exibe as coordenadas no terminal
    print(f"Ponto mais alto: {highest_point}")
    print(f"Ponto mais baixo: {lowest_point}")

# Função para plotar os pontos da circunferência usando simetria
def plot_circle_points(center_x, center_y, x, y):
    canvas.create_oval(center_x + x, center_y + y, center_x + x + 1, center_y + y + 1, fill="blue", outline="blue", tags="circle")
    canvas.create_oval(center_x - x, center_y + y, center_x - x + 1, center_y + y + 1, fill="blue", outline="blue", tags="circle")
    canvas.create_oval(center_x + x, center_y - y, center_x + x + 1, center_y - y + 1, fill="blue", outline="blue", tags="circle")
    canvas.create_oval(center_x - x, center_y - y, center_x - x + 1, center_y - y + 1, fill="blue", outline="blue", tags="circle")

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
canvas.pack()

window.mainloop()
