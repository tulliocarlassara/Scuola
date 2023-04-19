import matplotlib.pyplot as plt
from matplotlib import cm
import numpy as np
import warnings
warnings.filterwarnings("ignore") #scorciatoia per non gestire le divisioni per 0

#dati motore
f = 50     #[Hz]
n_cp = 1
V1 = 230   #[V]
k = 2.5
R0 = 625   #[Ω]
L0 = 0.05  #[H]
R1 = 0.5   #[Ω]
L1 = 0.02  #[H]
R2 = 0.2   #[Ω]
L2 = 0.002  #[H]

#scegli il campo di valori entro cui varia n_R
n_R_min = 0
n_R_max = 3000

X0 = 2*np.pi*f*L0
X1 = 2*np.pi*f*L1
X2 = 2*np.pi*f*L2

n_R = np.linspace(n_R_min,n_R_max,1000)
n_CMR = 60*f/n_cp

s = (n_CMR-n_R)/n_CMR

Z = R2 * (1-s)/s

A = 1+(R1+X1*1j)*(1/(X0*1j)+1/R0)
B = (R1+X1*1j)/k
C = 1/(R2+X2*1j+Z)*1/(k*A)

V2 = Z*C/(1+B*C)*V1
I2 = V2/Z
I1 = 1/A*(V1-B*I2)*(1/(X0*1j)+1/R0)+I2/k

#potenza assorbita
P1 = 3 * (V1 * I1.conjugate()).real
#potenza erogata
P2 = 3 * (V2 * I2.conjugate()).real
#coppia erogata
momento = P2 / (2*np.pi*f*(1-s))
#rendimento
rendimento = P2/P1

fig = plt.figure(figsize=(10,8))
ax = fig.add_subplot(311)
ax.grid()
#ax.set_xlabel('$n_R\ [g/min]$',fontsize=15)
ax.set_ylabel('$momento\ [N m]$',fontsize=15)
ax.plot(n_R,momento)

ax2 = fig.add_subplot(312)
ax2.grid()
#ax2.set_xlabel('$n_R\ [g/min]$',fontsize=15)
ax2.set_ylabel('$corrente\ [A]$',fontsize=15)
ax2.plot(n_R,abs(I1), label = '$I_1$ statore', color = 'orange')
ax2.plot(n_R,abs(I2), label = '$I_2$ rotore', color = 'purple')
ax2.legend(fontsize = 15)

#limito i risultati del rendimento a valori compresi tra 0 e 1 (se fuori dal campo inserisco valore 0)
rendimento = np.where((rendimento >= 0) & (rendimento <1),rendimento,0)
ax3 = fig.add_subplot(313)
ax3.grid()
ax3.set_xlabel('$n_R\ [g/min]$',fontsize=15)
ax3.set_ylabel('$\eta$',fontsize=15)
ax3.plot(n_R,rendimento, color = 'red')

plt.show()


