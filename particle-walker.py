import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

Nw = 125         # número de moléculas CS
snaps = 5000      # número de snapshots
Npick = 25       # número da molécula selecionada
length = 0.0     # comprimento
lmin = 1000.0    # valor mínimo
lmax = -1000.0   # valor máximo

xx = np.zeros((Nw, snaps), dtype=np.float64)
yy = np.zeros((Nw, snaps), dtype=np.float64)
zz = np.zeros((Nw, snaps), dtype=np.float64)

# Lê o arquivo de coordenadas XYZ
with open('/media/walas-bordinlab/data/ben_certo/70/dump2/dump2(temp-2.05).xyz', 'r') as file:
    for j in range(snaps):
        _ = file.readline()  # Ignora a primeira linha
        _ = file.readline()  # Ignora a segunda linha
        for i in range(Nw):
            line = file.readline().split()
            tdumb, xx[i, j], yy[i, j], zz[i, j] = line[0], float(line[1]), float(line[2]), float(line[3])
            if xx[i, j] > lmax:
                lmax = xx[i, j]
            if yy[i, j] > lmax:
                lmax = yy[i, j]
            if zz[i, j] > lmax:
                lmax = zz[i, j]
            if xx[i, j] < lmin:
                lmin = xx[i, j]
            if yy[i, j] < lmin:
                lmin = yy[i, j]
            if zz[i, j] < lmin:
                lmin = zz[i, j]

length = lmax - lmin

# Calcula as diferenças nas coordenadas em relação ao snapshot inicial
dx = xx[Npick, :] - xx[Npick, 0]
dx = dx - np.round(dx / length) * length
dy = yy[Npick, :] - yy[Npick, 0]
dy = dy - np.round(dy / length) * length
dz = zz[Npick, :] - zz[Npick, 0]
dz = dz - np.round(dz / length) * length

# Dividindo em cinco partes
n = snaps // 5
dx1, dy1, dz1 = dx[:n], dy[:n], dz[:n]
dx2, dy2, dz2 = dx[n:2*n], dy[n:2*n], dz[n:2*n]
dx3, dy3, dz3 = dx[2*n:3*n], dy[2*n:3*n], dz[2*n:3*n]
dx4, dy4, dz4 = dx[3*n:4*n], dy[3*n:4*n], dz[3*n:4*n]
dx5, dy5, dz5 = dx[4*n:], dy[4*n:], dz[4*n:]

# Plota o gráfico 3D com pontos e cores diferentes para cada parte
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.legend(loc='center left')
ax.scatter(dx1, dy1, dz1, color='black', label='Parte 1')
ax.scatter(dx2, dy2, dz2, color='violet', label='Parte 2')
ax.scatter(dx3, dy3, dz3, color='blue', label='Parte 3')
ax.scatter(dx4, dy4, dz4, color='red', label='Parte 4')
ax.scatter(dx5, dy5, dz5, color='orange', label='Parte 5')

ax.set_xlabel('\u0394 X')
ax.set_ylabel('\u0394 Y')
ax.set_zlabel('\u0394 Z')
ax.legend()  # Adiciona legenda ao gráfico
# Salva a imagem em um arquivo
plt.savefig('trajetoria_molecula-temp-2.05.png')
plt.show()


