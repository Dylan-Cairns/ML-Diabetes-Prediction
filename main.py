from flask import Flask, render_template, flash, Markup
import pickle
import numpy
from form import DiagnoseForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
model = pickle.load(open('rf_model.pkl', 'rb'))


@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("home.html", title='Home')


@app.route("/diagnose", methods=['GET', 'POST'])
def diagnose():
    form = DiagnoseForm()
    if form.validate_on_submit():
        gender = (form.gender.data == 'True') # Convert boolean to string
        polyuria = form.polyuria.data
        polydipsia = form.polydipsia.data
        sudden_wl = form.sudden_wl.data
        obesity = form.obesity.data
        features = [gender, polyuria, polydipsia, sudden_wl, obesity]
        prediction = 'Positive' if model.predict([features]) else 'Negative' # Convert boolean to string
        accuracy = round((numpy.max(model.predict_proba([features])) / 1), 2)
        flash(Markup(render_template("result.html", prediction=prediction, accuracy=accuracy)))
        return render_template("diagnose.html", form=form, title='Diagnose')
    return render_template("diagnose.html", form=form, title='Diagnose')


@app.route("/data")
def data():
    return render_template("data.html", title='Data')


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == "__main__":
    app.run()
