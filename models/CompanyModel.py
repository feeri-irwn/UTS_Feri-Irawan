from config import db

class Company(db.Model):
    __tablename__ = 'companies'

    # Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    industry = db.Column(db.String(80), nullable=True)

    # Add a __repr__ method to help with object representation
    def __repr__(self):
        return f"<Company {self.id}: {self.name}, {self.industry}>"
