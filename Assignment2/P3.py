"""
P3. Minimization with Gradient Descend.
Student name: Kasidit Chomputhong
"""
import numpy as np

def gmin(u0, lr, N):
    u = u0
    for i in range(N):
        functionG = (8*(np.exp(-8*u))/(np.exp(-8*u)+1)**2) - (np.exp(-u)/(np.exp(-u)+1)**2)
        u = u - lr * functionG
    return np.round(u,12)

if __name__ == "__main__":
    ux = gmin(u0=0, lr=0.2, N=10)
    print(ux)