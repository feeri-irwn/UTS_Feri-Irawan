from config import db

class Task(db.Model):
    __tablename__ = 'tasks'

    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)

    employee = db.relationship('Employee', backref='tasks', lazy=True)

    def __repr__(self):
        return f"<Task {self.id}: {self.description}, Employee {self.employee.name}>"
