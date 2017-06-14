import googlemaps
import requests

def run():
   x = True

   while True:
       travel_guide()

def weather(country, city):   

    # Function that returns the temperature, humidity and local time
     
    weather_data = requests.get("http://api.wunderground.com/api/2ddcf526ba46b259/conditions/q/{0}/{1}.json".format(country,city))
   
    temp = weather_data.json()['current_observation']['temp_c']
    humidity = weather_data.json()['current_observation']['relative_humidity']
    local_time = weather_data.json()['current_observation']['local_time_rfc822']
    print("Temperature:" + str(temp), "Humidity:" + str(humidity), "Local time:" + str(local_time))
    print('\n')
    print('Enjoy your travel :-)\n')
    print('--------------------------------------------------------------------')
def geometry(input_value):
       
    # Function that gets the latitude and longitude    
    
        google_api_key = 'AIzaSyDTjbpnpFBeB03oW-DeorPtsGgfeVlswes'
        gm = googlemaps.Client(key=google_api_key)
        geocode_result = gm.geocode(input_value)[0]
        latitude = geocode_result['geometry']['location']['lat']
        longitude = geocode_result['geometry']['location']['lng']
        print('\n')
        print('The Location is:\n')
        print("Latitude:" + str(latitude), "Longitude:" + str(longitude))
        print('\n')
def travel_guide():
    
    # function to call  the weather and geometric methods
    country = input('Which Country do you wish to travel to?\n\n')
    if isinstance(country, str):        
        city = input('Which city? \n\n')
        if isinstance(city, str):         
            
            geometry(city)
            weather(country, city)
        else:
               print('Invalid input') 
    else:
               print('Invalid input')  
    
run()
