# Tentativa corrigida: gerar frames manualmente, convertê-los em imagens PIL e salvar como GIF.
# Isso evita problemas com writers que dependem de backends.
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import io
import os

# Configurações
WIDTH, HEIGHT = 720, 1280
DPI = 100
fig = plt.figure(figsize=(WIDTH/DPI, HEIGHT/DPI), dpi=DPI)
ax = fig.add_axes([0, 0, 1, 1])
ax.set_xlim(0, WIDTH)
ax.set_ylim(0, HEIGHT)
ax.axis('off')

# Parâmetros da hélice
num_rungs = 36
y = np.linspace(220, HEIGHT-220, num_rungs)
amp = 120
freq = 2 * np.pi / 140
phase_speed = 0.18
strand_offset = np.pi

# criar artistas
line1, = ax.plot([], [], linewidth=8, solid_capstyle='round')
line2, = ax.plot([], [], linewidth=8, solid_capstyle='round')
rungs_lines = [ax.plot([], [], linewidth=4, solid_capstyle='round')[0] for _ in range(num_rungs)]
ax.add_patch(plt.Rectangle((0,0), WIDTH, HEIGHT, color=(0.03,0.03,0.07), zorder=0))

frames = 120
pil_frames = []

for frame in range(frames):
    phase = frame * phase_speed
    x1 = WIDTH/2 + amp * np.cos(freq * y + phase)
    x2 = WIDTH/2 + amp * np.cos(freq * y + phase + strand_offset)
    
    line1.set_data(x1, y)
    line2.set_data(x2, y)
    line1.set_color((0.2, 0.8, 0.9))
    line2.set_color((0.9, 0.4, 0.7))
    
    for i, rung in enumerate(rungs_lines):
        rung.set_data([x1[i], x2[i]], [y[i], y[i]])
        rung.set_color((0.95, 0.95, 1.0))
        rung.set_alpha(0.9 - 0.4 * np.sin((i*0.6) + phase))
    
    # desenhar canvas e capturar como imagem
    fig.canvas.draw()
    buf = fig.canvas.tostring_rgb()
    ncols, nrows = fig.canvas.get_width_height()
    img = Image.frombytes("RGB", (ncols, nrows), buf)
    pil_frames.append(img.copy())

# salvar GIF
gif_path = "/mnt/data/dna_mobile.gif"
pil_frames[0].save(gif_path, save_all=True, append_images=pil_frames[1:], duration=33, loop=0)

# fechar figura
plt.close(fig)

# confirmar arquivo
print("Gerado:", gif_path, " — frames:", len(pil_frames))
# exibir primeira frame inline
display(pil_frames[0])


