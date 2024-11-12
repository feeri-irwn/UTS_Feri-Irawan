from config import db

class Address(db.Model):
    __tablename__ = 'addresses'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(120), nullable=False)
    city = db.Column(db.String(80), nullable=False)
    state = db.Column(db.String(80), nullable=True)
    zip_code = db.Column(db.String(10), nullable=True)

    # Add a __repr__ method to help with object representation
    def __repr__(self):
        return f"<Address {self.id}: {self.street}, {self.city}, {self.state}, {self.zip_code}>"
