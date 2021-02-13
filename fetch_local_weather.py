from requests import get
import json
from pprint import pprint
from haversine import haversine
from temperature_conversion import fahr_to_celsius


stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'


my_lat = 51.000386
my_lon = -0.079012


all_stations = get(stations).json()['items']


def find_closest():
    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']

        return closest_station


closest_stn = find_closest()
#sets URL
weather = weather + str(closest_stn)
#produces list
my_weather = get(weather).json()['items']
#converts to string
jsonString = json.dumps(my_weather)
#converts to json
ListOfFilteredKeys = json.loads(jsonString)
#matches value based on Key.
keyLookup = 'ambient_temp'
#matches value based on Key.
values_of_key = [a_dict[keyLookup] for a_dict in ListOfFilteredKeys]
#reduces new list to single string
mix_list = values_of_key
delimiter = ' '
# Convert list of items to a string value
final_str = delimiter.join(map(str, mix_list))
# Convert String to float
MyTemperature = float(final_str)
# calls function to convert Fahrenheit to Celsius and compares to my defined temp. If it is less that x degrees Prints it is cold.
if fahr_to_celsius(MyTemperature) < 7:
    print("It is cold")
elif fahr_to_celsius(MyTemperature) > 7:
  print("it is hot")
