from flask import Flask, render_template, request

from form import InputForm
#from computing import plot_image
from model import Lorentz

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
    app.run(debug=True)