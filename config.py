from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://FeriIrawan_occurthou:a3ad6789f580535d35019177b86e7f5026ea3265@r2-t4.h.filess.io:3307/FeriIrawan_occurthou'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 3,
    'max_overflow': 0,
    'pool_timeout': 30 
}

db = SQLAlchemy(app)

app.app_context().push()
