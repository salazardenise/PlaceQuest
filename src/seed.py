"""This script seeds the database for the PlaceQuest app"""

# standard imports
import os
import sys


# model.py imports
from model import (Facility, Speciality, Condition, Insurance)
from model import (FacilitySpeciality, FacilityCondition, FacilityInsurance)
from model import connect_to_db, db
from server import app


def load_dummy_data():
    """Load dummy data to database"""

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

    s1 = Speciality(name='Assisted Living Facility')
    s2 = Speciality(name='Custodial Care Facility')
    s3 = Speciality(name='Hospice')
    s4 = Speciality(name='Skilled Nursing Facility')

    f4.specialities.append(s4)
    f5.specialities.append(s4)
    f6.specialities.append(s4)
    f7.specialities.append(s4)
    f8.specialities.append(s4)
    f9.specialities.append(s4)
    f10.specialities.append(s4)
    f11.specialities.append(s4)

    c1 = Condition(name='Stroke')
    c2 = Condition(name='Nervous System Disorder')
    c3 = Condition(name='Brain Disease or Condition')
    c4 = Condition(name='Spinal Cord Disease or Condition')
    c5 = Condition(name='Hip or Femur Fracture')
    c6 = Condition(name='Amputation or Joint Condition')
    c7 = Condition(name='Other Conditions')

    f4.conditions.append(c6)
    f5.conditions.append(c6)
    f6.conditions.append(c6)
    f7.conditions.append(c6)
    f8.conditions.append(c6)
    f9.conditions.append(c6)
    f10.conditions.append(c6)
    f11.conditions.append(c6)

    i1 = Insurance(name='United Health Care')
    i2 = Insurance(name='Kaiser')
    i3 = Insurance(name='Aetna')
    i4 = Insurance(name='Medicare')
    i5 = Insurance(name='Medicaid')
    i6 = Insurance(name='No Insurance')

    f4.insurances.append(i5)
    f5.insurances.append(i5)
    f6.insurances.append(i5)
    f7.insurances.append(i5)
    f8.insurances.append(i5)
    f9.insurances.append(i5)
    f10.insurances.append(i5)
    f11.insurances.append(i5)

    db.session.add_all([f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11, f12, f13])
    db.session.commit()

    db.session.add_all([s1, s2, s3, s4])
    db.session.commit()

    db.session.add_all([c1, c2, c3, c4, c5, c6, c7])
    db.session.commit()

    db.session.add_all([i1, i2, i3, i4, i5, i6])
    db.session.commit()

if __name__ == '__main__':
    connect_to_db(app)

    # create the tables
    db.create_all()

    # import dummy data
    load_dummy_data()
   