from flask import Flask


app = Flask(__name__)
# from config import Config

# def create_app(config_class=Config):
#     app = Flask(__name__)
#     app.config.from_object(config_class)




from application import models