import os
from flask import Flask, render_template, request

#from form import InputForm
#from computing import plot_image
#from model import Lorentz

### MODEL ###

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

###

### FORMULARIO ###
from wtforms import Form, FloatField, validators

class InputForm(Form):
    x0 = FloatField(label='condição inicial em x', default=1.00)
    y0 = FloatField(label='condição inicial em y', default=1.01)
    z0 = FloatField(label='condição inicial em z', default=1.10)

    tf = FloatField(label='Intervalo de integração', default=500.0)

    s = FloatField(label='parâmetro s', default=10.0)
    r = FloatField(label='parâmetro r', default=28.0)
    b = FloatField(label='parâmetro b', default=8.0/3.0)
    
###

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    form = InputForm(request.form)
    if request.method == 'POST':
        lorentz = Lorentz(form.x0.data, form.y0.data, form.z0.data,
                           form.tf.data, form.s.data, form.r.data, form.b.data)

        result = lorentz.plot_image()
    else:
        result = None

    return render_template('view.html', form=form, result=result)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)