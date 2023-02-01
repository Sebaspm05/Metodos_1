# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 09:45:20 2023

@author: j.pabonm
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim


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
        
    def Evolution (self,i):
        self.SetVelocity(i)
        
    def Setposition(self,i):
        self.R[i]=self.r
        
    def GetPosition (self,scale=1):
        return self.R[::scale]
    
    def SetVelocity(self,i):
        self.V[i]=self.v
        
    def GetVelocity (self,scale=1):
        return self.R[::scale]
    
def Runsimulation(t):
    
    r0=np.array([0.1,0.1])
    v0=np.array([1,5])
    a0=np.array([0,-9.8])
    
    p1= Particle(r0,v0,a0,t)
            
"__init__ : "

"self.atributo de un objeto"
    
t=np.linspace(0, 1,10)
p1= Particle([0,0], [1,0], [0,0], t)

velocity= p1.SetVelocity(3) 
"El numero en dentro del parentisis es el salto entre la matriz"


dt=0,1
tmax=1
t=np.arrage(0,tmax,dt)
Particles = Runsimulation(t)

fig= plt.figure(figsize=(5,5))
ax= fig.add_subplot(111)

def init():
    ax.set_xlimit(-10,10)
    ax.set_ylimit(-10,10)
    
def Update(i):
    ax.clear()
    init()
    
    x= Particles.GetPosition()[i,0]
    y= Particles.GetPosition()[i,1]
     
    vx= Particles.GetVelocity()[i,0]
    vy= Particles.GetVelocity()[i,1]
    
    circle = plt.Circle((x,y),Particles.radius, fill=True)
    ax.add_patch(circle)
    
    ax.arrow( x,y,vx,vy,head_width=0.2,color='r' )
    
Animation = anim.FuncAnimation(fig,Update,frames=len(t),init_func=init)


    

