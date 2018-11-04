# -*- coding: utf-8 -*-
from io import BytesIO
import base64

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

class Lorentz:
    def __init__(self, x0=1.0, y0=1.01, z0=1.1, tf=500, s=10.0, r=28.0, b=8.0/3.0):
        # Condições iniciais
        self.inic = [x0, y0, z0]        
        
        # Intervalo de integração [0, tf]
        self.t = np.linspace(0, tf, 10000)
        
        # Parâmetros
        self.s = s#10.0
        self.r = r#28.0
        self.b = b#8.0/3.0

    def lorentz(self, u, time):
        dx = self.s*( u[1] - u[0] )
        dy = u[0]*( self.r - u[2] ) - u[1]
        dz = u[0]*u[1] - self.b*u[2]
        return [dx, dy, dz]

    def result_model(self):
        return odeint(self.lorentz, self.inic, self.t)

    def plot_image(self):
        func = self.result_model()
        img = BytesIO()

        plt.subplot(3,1,1)
        plt.plot(self.t, func[:,0])
        plt.ylabel('x', fontsize=16)    

        ax2 = plt.subplot(3,1,2)
        plt.plot(self.t, func[:,1])
        plt.ylabel('y', fontsize=16)

        plt.subplot(3,1,3)
        plt.plot(self.t, func[:,2])
        plt.ylabel('z', fontsize=16)
        plt.xlabel('time', fontsize=16)
    
        plt.savefig(img, format='png')
        img.seek(0)
        plot = base64.b64encode(img.getvalue()).decode('ascii')
        img.close()
        plt.close()
        return plot


# Caso queira visualizar os plot's 
def plot():
    lorentz = Lorentz()
    res = lorentz.result_model()

    plt.subplot(3,1,1)
    plt.plot(lorentz.t, res[:,0])
    plt.ylabel('x', fontsize=16)    

    plt.subplot(3,1,2)
    plt.plot(lorentz.t, res[:,1])
    plt.ylabel('y', fontsize=16)

    plt.subplot(3,1,3)
    plt.plot(lorentz.t, res[:,2])
    plt.ylabel('z', fontsize=16)
    plt.xlabel('time', fontsize=16)
    
    plt.show()

#plot()