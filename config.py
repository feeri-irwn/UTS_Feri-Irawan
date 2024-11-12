from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://UTSFeriIrawan0619_moonrecent:be64c1c79667ab59242762e97125b322d0f4ae3d@pys1s.h.filess.io:3306/UTSFeriIrawan0619_moonrecent'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()