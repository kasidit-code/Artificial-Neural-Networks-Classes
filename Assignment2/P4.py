"""
P4. Maximization with Gradient Descend.
Student name: Kasidit Chomputhong
"""
import numpy as np

def gmax(u0, lr, N):
    u = u0
    for i in range(N):
        functionG = (-2*u) + 3
        u = u + lr * functionG
    return np.round(u,12)

if __name__ == "__main__":
    ux = gmax(u0=0, lr=0.2, N=10)
    print(ux)