from flask import Flask
from config import Config
import pickle

# start application
app = Flask(__name__)

# import configuration
app.config.from_object(Config)

# load machine learning model
model = pickle.load(open('app/static/rf_model.pkl', 'rb'))

from app import routes

