# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:45:20 2023

@author: j.pabonm
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
"from tqdm import tqdm"

"Clase: Crear objeto(Instancía) -Constructor, -Atributos, -Metodos"

class Particle:
    def __init__(self, r0,v0,a0,t,m=1,radius=0.3,Id=0):
        self.dt=t[1]-t[0]

        self.r=r0
        self.v=v0
        self.a=a0
        
        self.R= np.zeros((len(t),len(r0)))
        self.V= np.zeros_like(self.R)
        self.A= np.zeros_like(self.R)
        
        self.radius = radius
        self.masa = m
        
    
    def Setposition(self,i):
        self.R[i]=self.r
        
    def GetPosition (self,scale=1):
        return self.R[::scale]
    
    def SetVelocity(self,i):
        self.V[i]=self.v
        
    def GetVelocity (self,scale=1):
        return self.R[::scale]
    
def Runsimulation(t):
    
    r0=np.zeros([0.1,0.1])
    v0=np.zeros([1,5])
    a0=np.zeros([0,0])
    
        
"__init__ : "

"self.atributo de un objeto"
    
t=np.linspace(0, 1,10)
p1= Particle([0,0], [1,0], [0,0], t)

p1.GetVelocity(3) 
"El numero en dentro del parentisis es el salto entre la matriz"




print(p1.r)
print(p1.v)
print(p1.V)
print(p1.radius)
print(p1.R)

