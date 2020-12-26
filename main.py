from flask import Flask, render_template
import pickle
from form import DiagnoseForm
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'
model = pickle.load(open('rf_model.pkl', 'rb'))
bootstrap = Bootstrap(app)


@app.route("/", methods=['GET', 'POST'])
def home():
    form = DiagnoseForm()
    if form.validate_on_submit():
        gender = form.gender.data
        polyuria = form.polyuria.data
        polydipsia = form.polydipsia.data
        sudden_wl = form.sudden_wl.data
        obesity = form.obesity.data
        features = [gender, polyuria, polydipsia, sudden_wl, obesity]
        prediction = model.predict([features])
        return render_template("home.html", form=form, data=prediction)
    return render_template("home.html", form=form, data='')

@app.route("/diagnose", methods=['GET', 'POST'])
def diagnose():
    form = DiagnoseForm()
    if form.validate_on_submit():
        gender = (form.gender.data == 'True')
        polyuria = form.polyuria.data
        polydipsia = form.polydipsia.data
        sudden_wl = form.sudden_wl.data
        obesity = form.obesity.data
        features = [gender, polyuria, polydipsia, sudden_wl, obesity]
        prediction = model.predict([features])
        return render_template("diagnose.html", form=form, data=prediction)
    return render_template("diagnose.html", form=form, data='')


@app.route("/data")
def data():
    return render_template("data.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run()