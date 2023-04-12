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

ReZ = np.linspace(0,100,100)
ImZ = np.linspace(-100,100,200)

ReZ, ImZ = np.meshgrid(ReZ,ImZ)

Z = ReZ+ImZ*1j

A = 1+(R1+X1*1j)*(1/(X0*1j)+1/R0)
B = (R1+X1*1j)/m
C = 1/(R2+X2*1j+Z)*1/(m*A)

V2 = Z*C/(1+B*C)*V1
I2 = V2/Z

I1 = 1/A*(V1-B*I2)*(1/(X0*1j)+1/R0)+I2/m

η = np.real(V2*np.conj(I2))/np.real(V1*np.conj(I1))

fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('$Re(\dot Z)$', fontsize=20)
ax.set_ylabel('$Im(\dot Z)$', fontsize=20)
ax.zaxis.set_rotate_label(False) 
ax.set_zlabel('$\eta$', fontsize=20)
surf = ax.plot_surface(ReZ, ImZ, η, cmap=cm.jet, linewidth=0.3)
fig.colorbar(surf, shrink=0.5, aspect=10)
ax.view_init(30, 130)
plt.show()
