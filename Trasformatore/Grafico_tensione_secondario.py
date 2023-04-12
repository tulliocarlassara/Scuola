import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

#dati trasformatore
R0 = 10000
R1 = 10
R2 = 0.6
X0 = 5000
X1 = 20
X2 = 1.5
m = 4.348

#tensione al primario
V1 = 1000

ReZ = np.linspace(0,10,100)
ImZ = np.linspace(-10,10,200)

ReZ, ImZ = np.meshgrid(ReZ,ImZ)

Z = ReZ+ImZ*1j

A = 1+(R1+X1*1j)*(1/(X0*1j)+1/R0)
B = (R1+X1*1j)/m
C = 1/(R2+X2*1j+Z)*1/(m*A)

V2 = Z*C/(1+B*C)*V1

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('$Re(\dot Z)$', fontsize=20)
ax.set_ylabel('$Im(\dot Z)$', fontsize=20)
ax.zaxis.set_rotate_label(False) 
ax.set_zlabel('$|\dot V_2|$', fontsize=20)
surf = ax.plot_surface(ReZ, ImZ, np.abs(V2), cmap=cm.jet, linewidth=0.3)
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.view_init(40, 140)
plt.show()
