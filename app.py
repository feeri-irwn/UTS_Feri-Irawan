from config import app, db
from routes.Address_bp import address_bp
from routes.Company_bp import company_bp
from routes.Employee_bp import employee_bp
from routes.Task_bp import task_bp


app.register_blueprint(address_bp)
app.register_blueprint(company_bp)
app.register_blueprint(employee_bp)
app.register_blueprint(task_bp)

db.create_all()

@app.route('/')
def home():
    return "Selamat datang :), Saya Feri Irawan 21.83.0619"

if __name__ == '__main__':
    app.run(debug=True)
