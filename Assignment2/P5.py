"""
P5. Two-Decimensional Problem with Gradient Descend.
Student name: Kasidit Chomputhong
"""
import numpy as np

def grad_g(u):
    assert u.shape == (2,1)
    gradu =  np.array([[2*u[0,0] + 1.5*u[1,0] - 16],
                        [4*u[1,0] + 1.5*u[0,0] - 35]])

    return gradu
def g2min(u0,lr,N):
    u = u0
    for i in range(N):
        u = u - lr * grad_g(u)
    return np.round(u,12)

if __name__ == "__main__":
    u0= np.array([[0],[0]])
    ux = g2min(u0, lr=0.1, N=50)
    print("u*=", ux)