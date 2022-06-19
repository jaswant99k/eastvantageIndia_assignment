import requests
import json
from sqlalchemy.orm import Session
import geopy.distance


"""
Session manages persistence operations for ORM-mapped objects.
Let's just refer to it as a database session for simplicity
"""

from app.models import Address

def get_lat_lang(ip):
	response = requests.get("https://geolocation-db.com/json/"+ip+"&position=true").json()
	return (str(response['latitude'])+"$"+str(response['longitude']))





def create_address(db:Session, first_name, last_name, age, phone_no, email, ip):
	lat_lang = get_lat_lang(ip)
	
    # create address instance 
	new_address = Address(first_name=first_name, last_name=last_name, age=age, phone_no=phone_no,email=email, lat_lang = lat_lang )
    #place object in the database session
	db.add(new_address)
    #commit your instance to the database
	db.commit()
    #refresh the attributes of the given instance
	db.refresh(new_address)
	return new_address

def get_address(db:Session, ip:str, distance:int):
	"""
    get the first record with a given id, if no such record exists, will return null
    """
	current_location = get_lat_lang(ip).replace("$", ",")
	db_address = db.query(Address).all()
	available_address = []
	for a in db_address:
		#print(a.lat_lang.replace("$", ","))
		coords_1 = current_location
		coords_2 = a.lat_lang.replace("$", ",")
		distance_in_km = geopy.distance.geodesic(coords_1, coords_2).km
		
		if distance_in_km<=distance:
			print(distance_in_km)
			available_address.append(a)
	return available_address