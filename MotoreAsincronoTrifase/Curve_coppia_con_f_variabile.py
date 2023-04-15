import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np

#dati motore
f_nom = 50     #[Hz]
n_cp = 1
V1_nom = 230   #[V]
k = 2.5
R0 = 625   #[Ω]
L0 = 0.05  #[H]
R1 = 0.5   #[Ω]
L1 = 0.02  #[H]
R2 = 0.2   #[Ω]
L2 = 0.002  #[H]

#scegli il campo di valori enrto cui varia f
f_min = 10
f_max = 60

#campo di valori entro cui varia n_R
n_R_min = 10
n_R_max = 60*f_max/n_cp

n_R = np.linspace(n_R_min,n_R_max,100)
f = np.linspace(f_min,f_max,100)

f, n_R = np.meshgrid(f,n_R)

#modifica lineare della tensione di alimentazione al variare di f
V1 = V1_nom * f/f_nom
V1 = np.where(V1<=V1_nom,V1,V1_nom)

X0 = 2*np.pi*f*L0
X1 = 2*np.pi*f*L1
X2 = 2*np.pi*f*L2

n_CMR = 60*f/n_cp

s = (n_CMR-n_R)/n_CMR

Z = R2 * (1-s)/s

A = 1+(R1+X1*1j)*(1/(X0*1j)+1/R0)
B = (R1+X1*1j)/k
C = 1/(R2+X2*1j+Z)*1/(k*A)

V2 = Z*C/(1+B*C)*V1
I2 = V2/Z

P2 = 3 * (V2 * I2.conjugate()).real
#coppia erogata
momento = P2 / (2*np.pi*f*(1-s))

momento = np.where(momento>=0,momento,0)


fig = plt.figure(figsize=(20,20))
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('$f$', fontsize=20)
ax.set_ylabel('$n_R$', fontsize=20)
ax.zaxis.set_rotate_label(False) 
ax.set_zlabel('$M$', fontsize=20)
surf = ax.plot_wireframe(f, n_R, momento, rstride=0, cstride=3)
ax.view_init(0, 0)
plt.show()
