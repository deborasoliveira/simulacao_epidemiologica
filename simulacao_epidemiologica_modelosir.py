import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parâmetros
grid_size = 50
beta = 0.3    # taxa de infecção
gamma = 0.05  # taxa de recuperação
steps = 100

# Estados: 0=Suscetível, 1=Infectado, 2=Recuperado
grid = np.zeros((grid_size, grid_size), dtype=int)

# Inicializa com 1 infectado no centro
grid[grid_size // 2, grid_size // 2] = 1

# Para armazenar resultados
frames = []

def update(frame_num):
    global grid
    new_grid = grid.copy()
    for i in range(grid_size):
        for j in range(grid_size):
            if grid[i, j] == 0:  # suscetível
                # Checa vizinhos infectados
                neighbors = grid[max(0, i-1):min(grid_size, i+2),
                                 max(0, j-1):min(grid_size, j+2)]
                if np.any(neighbors == 1):
                    if np.random.rand() < beta:
                        new_grid[i, j] = 1
            elif grid[i, j] == 1:  # infectado
                if np.random.rand() < gamma:
                    new_grid[i, j] = 2
    grid = new_grid
    mat.set_data(grid)
    return [mat]

# Visualização
fig, ax = plt.subplots()
mat = ax.matshow(grid, cmap='viridis', vmin=0, vmax=2)
ani = animation.FuncAnimation(fig, update, frames=steps, interval=200, repeat=False)
plt.show()
