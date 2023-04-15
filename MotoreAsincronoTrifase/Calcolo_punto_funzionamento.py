import numpy as np
from scipy.optimize import fsolve
from scipy.optimize import minimize

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

#valore desiderato del momento
M_resistente = 10 #[N*m]

X0 = 2*np.pi*f*L0
X1 = 2*np.pi*f*L1
X2 = 2*np.pi*f*L2

n_CMR = 60*f/n_cp

def momento(n_R):
    s = (n_CMR-n_R)/n_CMR

    Z = R2 * (1-s)/s

    A = 1+(R1+X1*1j)*(1/(X0*1j)+1/R0)
    B = (R1+X1*1j)/k
    C = 1/(R2+X2*1j+Z)*1/(k*A)

    V2 = Z*C/(1+B*C)*V1
    I2 = V2/Z

    #potenza erogata
    P2 = 3 * (V2 * I2.conjugate()).real
    #coppia erogata
    momento = P2 / (2*np.pi*f*(1-s))
    
    return momento

def f_for_minimize(n_R):
    return - momento(n_R)

def f_for_fsolve(n_R):
    return M_resistente - momento(n_R)

#numero di giri relativo alla coppia massima
#punto iniziale di ricerca a n_CMR/2
n_R_coppia_massima = minimize(f_for_minimize, n_CMR/2).x[0]
M_max = momento(n_R_coppia_massima)
print('Coppia massima di', M_max, 'a', n_R_coppia_massima, '[giri/min]')

if M_max >= M_resistente:
    #punto iniziale di ricerca nel valore medio tra n_CMR e n_R_coppia_massima
    n_R_primo_tentativo = (n_CMR + n_R_coppia_massima)/2
    n_R_punto_di_funzionamento = fsolve(f_for_fsolve, n_R_primo_tentativo)[0]
    print('M =', M_resistente, '[N*m] a', n_R_punto_di_funzionamento, '[giri/min]')
else:
    print('Il momento resistente supera il momento massimo disponibile')

