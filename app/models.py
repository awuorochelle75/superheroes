from app import db
from sqlalchemy.orm import validates


class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Hero {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "super_name": self.super_name
        }

class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Power {self.name}>"

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description
        }

    @validates('description')
    def validate_description(self, key, value):
        if not value or len(value.strip()) < 20:
            raise ValueError("Description must be at least 20 characters long.")
        return value


class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    def __repr__(self):
        return f"<HeroPower {self.strength}>"

    def to_dict(self):
        return {
            "id": self.id,
            "strength": self.strength,
            "power": self.power.to_dict()
        }

    @validates('strength')
    def validate_strength(self, key, value):
        allowed = ['Strong', 'Weak', 'Average']
        if value not in allowed:
            raise ValueError("Strength must be 'Strong', 'Weak', or 'Average'")
        return value
