"""This script seeds the database for the PlaceQuest app"""

# standard imports
import os
import sys

# third party imports
from flask_sqlalchemy import SQLAlchemy

""" This is the connection to the PostgreSQL database,
obtained through the Flask-SQLAlchemy helper library. """

db = SQLAlchemy()

##############################################################################
# Model definitions

class Facility(db.Model):
    """Health facility"""

    __tablename__ = 'facilities'

    facility_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)
    address = db.Column(db.String(500), nullable=False)
    city = db.Column(db.String(500), nullable=False)
    state = db.Column(db.String(500), nullable=False)
    zipcode = db.Column(db.String(500), nullable=False)
    phone = db.Column(db.String(500), nullable=False)
    fax = db.Column(db.String(500), nullable=False)
    npi = db.Column(db.String(500), nullable=False)
    likes = db.Column(db.Integer)
    dislikes = db.Column(db.Integer)
    stars = db.Column(db.Integer)

    specialities = db.relationship('Speciality', secondary='facilities_specialities')
    conditions = db.relationship('Condition', secondary='facilities_conditions')
    insurances = db.relationship('Insurance', secondary='facilities_insurances')

    def __repr__(self):
        return f'<Facility id:{self.facility_id} name:{self.name}>'

class Speciality(db.Model):
    """Speciality type"""

    __tablename__ = 'specialities'

    speciality_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)

    facilities = db.relationship('Facility', secondary='facilities_specialities')

    def __repr__(self):
        return f'<Speciality id:{self.speciality_id} name:{self.name}>'

class Condition(db.Model):
    """Medical Conditions types"""

    __tablename__ = 'conditions'

    condition_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)

    facilities = db.relationship('Facility', secondary='facilities_conditions')

    def __repr__(self):
        return f'<Condition id:{self.condition_id} name:{self.name}>'

class Insurance(db.Model):
    """Medical Conditions types"""

    __tablename__ = 'insurances'

    insurance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(500), nullable=False)

    facilities = db.relationship('Facility', secondary='facilities_insurances')

    def __repr__(self):
        return f'<Insurance id:{self.insurance_id} name:{self.name}>'

class FacilitySpeciality(db.Model):
    """Association table between Facility and Speciality"""

    __tablename__ = 'facilities_specialities'

    facility_speciality_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.facility_id'), nullable=False) 
    speciality_id = db.Column(db.Integer, db.ForeignKey('specialities.speciality_id'),nullable=False) 

    def __repr__(self):
        return f'<FacilitySpeciality facility_speciality_id:{self.facility_speciality_id} facility_id:{self.facility_id} speciality_id:{self.speciality_id}'

class FacilityCondition(db.Model):
    """Association table between Facility and Condition"""

    __tablename__ = 'facilities_conditions'

    facility_condition_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.facility_id'), nullable=False) 
    condition_id = db.Column(db.Integer, db.ForeignKey('conditions.condition_id'),nullable=False) 

    def __repr__(self):
        return f'<FacilityCondition facility_condition_id:{self.facility_condition_id} facility_id:{self.facility_id} condition_id:{self.condition_id}'

class FacilityInsurance(db.Model):
    """Association table between Facility and Insurance"""

    __tablename__ = 'facilities_insurances'

    facility_insurance_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    facility_id = db.Column(db.Integer, db.ForeignKey('facilities.facility_id'), nullable=False) 
    insurance_id = db.Column(db.Integer, db.ForeignKey('insurances.insurance_id'),nullable=False) 

    def __repr__(self):
        return f'<FacilityInsurance facility_insurance_id:{self.facility_insurance_id} facility_id:{self.facility_id} insurance_id:{self.insurance_id}'

##############################################################################
# Helper functions

def connect_to_db(app, db_uri="postgresql:///placequestdb"):
    """ Connect the database to the Flask app. """

    # Configure to use a PostgreSQL database
    app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    app.config['SQLALCHEMY_ECHO'] = False
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == '__main__':
    """ As a convenience, if we run this module interactively,
    this will allow the user to work with the database directly. """

    from server import app
    connect_to_db(app)
    print("Connected to DB.")
