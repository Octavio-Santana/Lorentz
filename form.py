from wtforms import Form, FloatField, validators

class InputForm(Form):
    x0 = FloatField(label='condição inicial em x', default=1.00)
    y0 = FloatField(label='condição inicial em y', default=1.01)
    z0 = FloatField(label='condição inicial em z', default=1.10)

    tf = FloatField(label='Intervalo de integração', default=500.0)

    s = FloatField(label='parâmetro s', default=10.0)
    r = FloatField(label='parâmetro r', default=28.0)
    b = FloatField(label='parâmetro b', default=8.0/3.0)