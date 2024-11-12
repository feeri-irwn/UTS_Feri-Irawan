from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://UTSFeriIrawan0619_borderhim:94544b17679e0f3a04f4d9cf1328f185e9615d4b@zf8c4.h.filess.io:3306/UTSFeriIrawan0619_borderhim'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

app.app_context().push()