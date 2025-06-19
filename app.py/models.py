from app import db

# Hero model
class Hero(db.Model):
    __tablename__ = 'heroes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    super_name = db.Column(db.String, nullable=False)

    # One Hero has many HeroPowers
    hero_powers = db.relationship('HeroPower', backref='hero', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Hero {self.name}>"

# Power model
class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)

    # One Power has many HeroPowers
    hero_powers = db.relationship('HeroPower', backref='power', cascade='all, delete-orphan')

    def __repr__(self):
        return f"<Power {self.name}>"

# HeroPower model (join table with extra column: strength)
class HeroPower(db.Model):
    __tablename__ = 'hero_powers'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String, nullable=False)

    hero_id = db.Column(db.Integer, db.ForeignKey('heroes.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    def __repr__(self):
        return f"<HeroPower {self.strength}>"
