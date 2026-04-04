from . import db

class Properties(db.Model):
    __tablename__ = 'properties'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    description = db.Column(db.String(255))
    bedrooms = db.Column(db.String(80))
    bathrooms = db.Column(db.String(80))
    price = db.Column(db.Float)
    property_type = db.Column(db.String(80))
    location = db.Column(db.String(80))
    image_file = db.Column(db.String(80))

    def __init__(self, title, description, bedrooms, bathrooms, price, property_type, location, image_file):
        self.title = title
        self.description = description
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.price = price
        self.property_type = property_type
        self.location = location
        self.image_file = image_file
