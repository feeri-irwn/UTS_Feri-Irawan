from config import db

class Employee(db.Model):
    __tablename__ = 'employees'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    address_id = db.Column(db.Integer, db.ForeignKey('addresses.id'), nullable=False)
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'), nullable=False)

    # Relationships
    address = db.relationship('Address', backref='employees', lazy=True)
    company = db.relationship('Company', backref='employees', lazy=True)

    # Add __repr__ method for better debugging and logging
    def __repr__(self):
        return f"<Employee {self.id}: {self.name}, {self.company.name}, {self.address.street}>"
