"""backend server for PlaceQuest App"""

# standard python imports
import json
import os

# third party imports
import requests
from jinja2 import StrictUndefined
from sqlalchemy import text
from flask import (Flask, render_template, redirect, request, flash, session, jsonify, url_for)
from flask_debugtoolbar import DebugToolbarExtension
from model import (Facility, Speciality, Condition, Insurance)
from model import (FacilitySpeciality, FacilityCondition, FacilityInsurance)
from model import connect_to_db, db

app = Flask(__name__)

# app.secret_key is required to use Flask sessions and the debug toolbar
app.secret_key = 'temporary_secret_key'

# set the following so that if an undefined variable is used in Jinja2,
# it doesn't fail silently
app.jinja_env.undefined = StrictUndefined


@app.route('/', methods=['GET'])
def index():
    """Display main page"""
    specialities = db.session.query(Speciality).all()
    conditions = db.session.query(Condition).all()
    insurances = db.session.query(Insurance).all()

    return render_template('main.html', 
                           facility_types=specialities,
                           conditions=conditions,
                           insurances=insurances)

def get_facilities(location, speicality, condition, insurance):
  # TODO: pull information from db rather than hardcode
    # db already set up, just need to set up sql joins

    f1 = Facility(name='Amazing Grace Oasis',
              address='8708 Bridgepoint Ave, Hesperia, CA 92344-5562',
              city='Hesperia', state='CA', zipcode='92344-5562',
              phone='818-572-3956', fax='818-572-3956',
              npi='1396213302', likes=0, dislikes=0, stars=4)
    f2 = Facility(name='Crestwood Behavioral Health Inc',
                  address='2600 Stockton Blvd, Sacramento, CA, 95817-2210',
                  city='Sacramento', state='CA', zipcode='95817-2210',
                  phone='916-452-1431', fax='916-452-2895',
                  npi='1356411656', likes=10, dislikes=2, stars=5)
    f3 = Facility(name='San Francisco Healing Center',
                  address='450 Stanyan St Fl 5, San Francisco, CA, 94117-1019',
                  city='San Francisco', state='CA', zipcode='94117-1019',
                  phone='209-955-2328', fax='209-644-5721',
                  npi='1447758024', likes=10, dislikes=2, stars=5)
    f4 = Facility(name='3556 Cesar Chavez',
                  address='3555 Cesar Chavez, San Francisco, CA94110-4403',
                  city='San Francisco', state='CA', zipcode='94110-4403',
                  phone='408-241-3844', fax='NA',
                  npi='1740309103', likes=10, dislikes=2, stars=5)
    f5 = Facility(name='A Grace Sub Acute & Skilled Care',
                  address='1250 S Winchester Blvd, San Jose, CA 96128-3906',
                  city='San Jose', state='CA', zipcode='95128-3906',
                  phone='408-241-3844', fax='408-241-3844',
                  npi='1689828840', likes=10, dislikes=2, stars=5)
    f6 = Facility(name='AHC Healthcare of Sacramento Corporation',
                  address='1411 Expo Pkwy, Sacramento, CA 95815',
                  city='Sacramento', state='CA', zipcode='95815',
                  phone='916-758-6300', fax='916-758-6350',
                  npi='1114439262', likes=10, dislikes=2, stars=5)
    f7 = Facility(name='Covia Communities',
                  address='1661 Pine St., San Francisco, CA 94109-0401',
                  city='San Francisco', state='CA', zipcode='94109-0401',
                  phone='415-776-0500', fax='415-776-5192',
                  npi='1982774329', likes=10, dislikes=2, stars=5)
    f8 = Facility(name='Laurel Heights Community Care',
                  address='2740 California St., San Francisco, CA, 94115-2514',
                  city='San Francisco', state='CA', zipcode='94115-2514',
                  phone='415-567-3133', fax='415-567-3037',
                  npi='1629476239', likes=10, dislikes=2, stars=5)
    f9 = Facility(name='Central Garden, Inc.',
                  address='1355 Ellis St., San Francisco, CA 94115-4215',
                  city='San Francisco', state='CA', zipcode='94115-4215',
                  phone='415-567-2967', fax='415-567-5933',
                  npi='1093872715', likes=10, dislikes=2, stars=5)
    f10 = Facility(name='Saint Francis Memorial Hospital',
                   address='900 Hyde St., San Francisco, CA 94019-4806',
                   city='San Francisco', state='CA', zipcode='94109-4806',
                   phone='415-353-6000', fax='415-353-6000',
                   npi='1861511206', likes=10, dislikes=2, stars=5)
    f11 = Facility(name='The Avenues Transitional Care Center',
                   address='2043 19th Ave, San Francisco, CA 94116-1253',
                   city='San Francisco', state='CA', zipcode='94116-1253',
                   phone='415-353-6000', fax='NA',
                   npi='1306360987', likes=10, dislikes=29, stars=5)
    f12 = Facility(name='Agesong Inc',
                   address='432 Ivy St., San Francisco, CA, 94102-4252',
                   city='San Francisco', state='CA', zipcode='94102-4254',
                   phone='415-431-8143', fax='415-431-1012',
                   npi='1356548135', likes=10, dislikes=18, stars=5)
    f13 = Facility(name='Laguna Grove Care',
                   address='624 Laguna Avenue, San Francisco, 94102',
                   city='San Francisco', state='CA', zipcode='94102',
                   phone='415-318-8870', fax='NA',
                   npi='1821295601', likes=2, dislikes=2, stars=5)

    facilities = [f4, f5, f6, f7, f8, f9, f10, f11]

    return facilities

@app.route('/results.json', methods=['GET'])
def get_results():

  # TODO: remove hardcode values, and get values from request
  location = 'san francisco'
  facility_type = 'Skilled Nursing Facility'
  condition = 'Amputation or Joint Condition'
  insurance = 'Medicaid'

  facilities = get_facilities(location, facility_type, condition, insurance)
  results = []
  for fac in facilities:
      results.append({'facility_id': fac.facility_id, 'name': fac.name, 'address': fac.address})

  return jsonify(results)


@app.route('/search', methods=['POST'])
def search():
    """Perform search and return place json results in results page"""
    location = request.form.get('location')
    facility_type = request.form.get('facility_type')
    condition = request.form.get('condition')
    insurance = request.form.get('insurance')

    location = '%%' + location + '%%'

    specialities = db.session.query(Speciality).all()
    conditions = db.session.query(Condition).all()
    insurances = db.session.query(Insurance).all()

    facilities = get_facilities(location, facility_type, condition, insurance)

    return render_template('results.html', 
                           facilities=facilities,
                           facility_types=specialities,
                           conditions=conditions,
                           insurances=insurances)


if __name__ == '__main__':
    # TODO: rmeove commented out code used for debugging during development
    # # debug must be set to True at the point that DebugToolbarExtension is invoked
    # app.debug = True
    # # make sure templates, etc. are not cached in debug mode
    # app.jinja_env.auto_reload = app.debug
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(port=5000, host='0.0.0.0')
