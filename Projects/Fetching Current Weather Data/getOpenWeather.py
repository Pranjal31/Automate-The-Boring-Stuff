#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

import sys, requests, json, datetime

API_KEY = '' #pranjal31 TODO: insert API key here
COORD_LIMIT = 1

if len(sys.argv) < 2:
    print('Usage: python3 getOpenWeather.py city_name, state code, 2-letter_country_code')
    sys.exit()
location = ' '.join(sys.argv[1:])


# fetch cooridinates for location
coord_url= f'http://api.openweathermap.org/geo/1.0/direct?q={location}&limit={COORD_LIMIT}&appid={API_KEY}'
response = requests.get(coord_url)
response.raise_for_status()
#print(response.text) # raw JSON

coord_json = json.loads(response.text)
if len(coord_json) == 0:
    print(f'ERROR: no cordinates available for {location}!')
    sys.exit()

lat = coord_json[0]['lat']
lon = coord_json[0]['lon']

# fetch weather data for coordinates
weather_url = f'https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={API_KEY}'
response = requests.get(weather_url)
response.raise_for_status()
#print(response.text) # raw JSON

dt_today = datetime.datetime.today()
today = dt_today.strftime('%Y-%m-%d')
today_plus_1 = (dt_today + datetime.timedelta(days=1)).strftime('%Y-%m-%d')
today_plus_2 = (dt_today + datetime.timedelta(days=2)).strftime('%Y-%m-%d')
today_done = False
today_plus_1_done = False
today_plus_2_done = False

# the output involves 3 hour forecast for the next few days. For simplicity, pick any random weather data point,
# from the options available, for a given day. In future, can make the weather data points consistent with respect to
# the time of the day
weather_json = json.loads(response.text)
for weather in weather_json['list']:
    if len(weather['weather']) == 0:
        print(f'ERROR: no weather data available for date: {weather["dt_txt"]}!')
        continue
    if today_done != True and weather['dt_txt'].split(' ')[0] == today:
        print('Current weather in ' + location + ':')
        print(weather['weather'][0]['main'] + ' - ' + weather['weather'][0]['description'])
        today_done = True
    elif today_plus_1_done != True and weather['dt_txt'].split(' ')[0] == today_plus_1:
        print('Tomorrow:')
        print(weather['weather'][0]['main'] + ' - ' + weather['weather'][0]['description'])
        today_plus_1_done = True
    elif today_plus_2_done != True and weather['dt_txt'].split(' ')[0] == today_plus_1:
        print('Day after tomorrow:')
        print(weather['weather'][0]['main'] + ' - ' + weather['weather'][0]['description'])
        today_plus_2_done = True
    elif today_plus_2_done == True and today_plus_1_done == True and today_done == True:
        break

    











