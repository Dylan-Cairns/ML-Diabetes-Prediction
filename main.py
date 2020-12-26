from flask import Flask, render_template
import pickle
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
        gender = (form.gender.data == 'True')
        polyuria = form.polyuria.data
        polydipsia = form.polydipsia.data
        sudden_wl = form.sudden_wl.data
        obesity = form.obesity.data
        features = [gender, polyuria, polydipsia, sudden_wl, obesity]
        prediction = model.predict([features])
        return render_template("diagnose.html", form=form, data=prediction, title='Diagnose')
    return render_template("diagnose.html", form=form, data='', title='Diagnose')


@app.route("/data")
def data():
    return render_template("data.html", title='Data')


@app.route("/about")
def about():
    return render_template("about.html", title='About')


if __name__ == "__main__":
    app.run()
