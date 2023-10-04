import tkinter as tk

# Função Bresenham para desenhar uma reta no primeiro e segundo oitante
def draw_line(x1, y1, x2, y2):
    x1 += canvas_width // 2  # Mapeia x1 para o centro do canvas
    y1 = canvas_height // 2 - y1  # Mapeia y1 para o centro do canvas
    x2 += canvas_width // 2  # Mapeia x2 para o centro do canvas
    y2 = canvas_height // 2 - y2  # Mapeia y2 para o centro do canvas

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    m = dy / dx if dx != 0 else None

    x, y = x1, y1
    points = []

    if m is None or m >= 1:
        d = 2 * dx - dy
        while y <= y2:
            points.append((x, y))
            if d >= 0:
                x += 1 if x1 < x2 else -1
                d -= 2 * dy
            y += 1
            d += 2 * dx
    else:
        d = 2 * dy - dx
        while x <= x2:
            points.append((x, y))
            if d >= 0:
                y += 1 if y1 < y2 else -1
                d -= 2 * dx
            x += 1 if x1 < x2 else -1
            d += 2 * dy

    print(f"Coordenadas da reta:")
    for point in points:
        x, y = point
        print(f"({int(x - canvas_width // 2)}, {int(canvas_height // 2 - y)})")
        canvas.create_oval(x, y, x, y, width=1, outline='black')

# Função para desenhar uma reta quando o botão é clicado
def draw_line_button():
    x1 = int(entry_x1.get())
    y1 = int(entry_y1.get())
    x2 = int(entry_x2.get())
    y2 = int(entry_y2.get())
    draw_line(x1, y1, x2, y2)

# Configuração da janela
window = tk.Tk()
window.title("Bresenham Line Drawing")

# Tamanho do canvas
canvas_width = 400
canvas_height = 400

# Configuração do canvas
canvas = tk.Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

# Desenha a linha x fixa (eixo x)
canvas.create_line(0, canvas_height // 2, canvas_width, canvas_height // 2, fill='blue')

# Desenha a linha y fixa (eixo y)
canvas.create_line(canvas_width // 2, 0, canvas_width // 2, canvas_height, fill='red')

# Entradas para as coordenadas
tk.Label(window, text="x1").pack()
entry_x1 = tk.Entry(window)
entry_x1.pack()

tk.Label(window, text="y1").pack()
entry_y1 = tk.Entry(window)
entry_y1.pack()

tk.Label(window, text="x2").pack()
entry_x2 = tk.Entry(window)
entry_x2.pack()

tk.Label(window, text="y2").pack()
entry_y2 = tk.Entry(window)
entry_y2.pack()

# Botão para desenhar a reta
draw_button = tk.Button(window, text="Desenhar Reta", command=draw_line_button)
draw_button.pack()

window.mainloop()
