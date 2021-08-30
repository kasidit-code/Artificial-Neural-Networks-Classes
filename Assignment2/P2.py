"""
P2. Loss and gradient.
Student name: Kasidit Chomputhong
"""
import numpy as np

def loss(u):
    return (1/(1+np.exp(-8*u)) - 1/(1+np.exp(-u)))

def grad(u):
    grad = (8*(np.exp(-8*u))/(np.exp(-8*u)+1)**2) - (np.exp(-u)/(np.exp(-u)+1)**2)
    return grad

if __name__ == "__main__":
    
    us = np.linspace(-1, 0, num=5)
    print(us)
    print(loss(us))
    print(grad(us))