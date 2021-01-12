from flask import Flask
from config import Config
import pickle


# Construct core Flask application.
def init_app():
    app = Flask(__name__)
    # import configuration
    app.config.from_object(Config)
    with app.app_context():
        # Import parts of our core Flask app
        from . import routes

        # Import Dash application
        from .plotlydash.dashboard import init_dashboard
        app = init_dashboard(app)

        return app


# load machine learning models
rf_model = pickle.load(open('app/data/rf_model.pkl', 'rb'))

