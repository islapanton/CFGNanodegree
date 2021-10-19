# APIs

### EXERCISE 1 ###
# """
# This API is called 'Open Notify' http://open-notify.org/
# It gives access to data about the Intrnational Space NASA station!
# This API DOES NOT require authentication,
#
# TASK: Make a call to the API endpoint to get live information about astronauts in space
#
# """
# Installing pip for api
import requests
from pprint import pprint as pp


endpoint1 = 'http://api.open-notify.org/astros.json'
# this endpoint returns data about astronauts currently in space

response = requests.get(endpoint1) # making a call to the API

print(response.status_code)  # make sure that your connection status code is 200, which means success!

data = response.json()  # lets see what data about people in space we get back from the API response
pp(data)

# let's extract data from the response and write it to a file
# we need section 'people' from json, which is a list of dict, so...
# we also need to extract name from each dict item in that list

with open('astronauts.txt', 'w') as text_file:
    for item in data['people']:
        text_file.write(item['name'] + '\n')
# added new line character, so each name appears on a new line.


### EXERCISE 2 ###
"""
TASK: Make a call with a 'PAYLOAD' (special requirements) to the API endpoint
"""

# this endpoint tells us timings when the international space station will pass over a **given location** on Earth
endpoint2 = 'http://api.open-notify.org/iss-pass.json'

# # As an input the API expects a latitude/longitude pair for the location of our interst
# # Let's make a dictionary with these parameters, and then include them into our call to the API
# these are coordinates for London
payload = {
    'lat': 51.507,
    'lon': 0.1278
}
payload = { # these are coordinates for New York
    'lat': 40.71,
    'lon': -74,
}

response = requests.get(endpoint2, params=payload)
print(response.status_code)

data = response.json()
pp(data)

 # Exercise 3
import requests
from datetime import datetime
from pprint import pprint as pp

# this endpoint tells the current location for international space station
endpoint3 = 'http://api.open-notify.org/iss-now.json'

response = requests.get(endpoint3)

data = response.json()
pp(data)

timestamp = data['timestamp']
dt_object = datetime.fromtimestamp(timestamp)

print("dt_object =", dt_object)
print("type(dt_object) =", type(dt_object))

msg = "At {dt} the ISS was passing the following location, latitude: {lat} and longitude: {lon}".format(
    dt = dt_object,
    lat = data['iss_position']['latitude'],
    lon = data['iss_position']['longitude'],
    # ADD CODE HERE # how do you think we print the message?
)
print(msg)

with open('space_station_location.txt', 'a') as text_file:
    text_file.write(msg + '\n')
