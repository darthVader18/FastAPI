# Python program to translate
# speech to text and text to speech


import speech_recognition as sr
import pyttsx3
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
#from translate import Translator
import requests
import configparser

# Function to convert text to
# speech
def SpeakText():
	
    # Initialize the recognizer
    r = sr.Recognizer()


	# Initialize the engine
	#engine = pyttsx3.init()
	#engine.say(command)
	#engine.runAndWait()
    
# Loop infinitely for user to
# speak

#while(1):	
	
    # Exception handling to handle
	# exceptions at the runtime
    try:
		
        # use the microphone as source for input.
        with sr.Microphone() as source2:
			
			# wait for a second to let the recognizer
			# adjust the energy threshold based on
			# the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Say Something")
			
			#listens for the user's input
            audio2 = r.listen(source2)
			
			# Using ggogle to recognize audio
            MyText = r.recognize_google(audio2)
            MyText = MyText.lower()
            
            return "Did you say " + MyText 
			#SpeakText(MyText)
            
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
		
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")



def time_zone(city_name):
     # initialize Nominatim API
    geolocator = Nominatim(user_agent="geoapiExercises")

    # getting Latitude and Longitud
    location = geolocator.geocode(city_name)

    # pass the Latitude and Longitud
    # into a timezone_at
    # and it return timezone
    obj = TimezoneFinder()

    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

    PARAMS = {
            'timezone': result,
            'token': 'aqulyBKQEzgWiZUdVmKp'
            }
    headers = {'Content-Type': 'application/json'}
    url = "https://timezoneapi.io/api/timezone/"
    response = requests.get(url, params = PARAMS, headers= headers).json()
    try:
        if response['meta']['code'] == "200":
            return f"""Time Zone: {result}\r\nDay : {response['data']['datetime']['day_full']}\r\nDate: {response['data']['datetime']['date']}\r\nTime: {response['data']['datetime']['time']}"""
        else:
            return "Please enter the correct location !"
    except:
        return "We are unable to process your request. Please try again in sometime"
        


def weather_by_city_name(city_name):
    PARAMS = {'q': city_name, 
            'appid': "15b853fddd039e2a6f81e81f32df79ae"
            }
    headers = {'Content-Type': 'application/json'}
    url = "http://api.openweathermap.org/data/2.5/weather"
    response = requests.get(url, params = PARAMS, headers= headers).json()
    try:
        if response["cod"] == 200:
            degree_sign = u"\N{DEGREE SIGN}"
            temperature_in_kelvin = response ['main']['temp']
            temperature_in_celsius = round(temperature_in_kelvin - 273.73)
            temperature_in_fahrenheit = round(temperature_in_celsius * 1.8 +32)
            
            return f"Temperature : {temperature_in_celsius} {degree_sign}C / {temperature_in_fahrenheit} {degree_sign}F" 
        else:
            return "Please enter the correct location !"
    except:
        return "We are unable to process your request. Please try again in sometime"



#def translate(lang_from, lang_to, text):
#    try:
#        #lang_from = input("From: ")
#        #lang_to = input("To: ")
#        translator= Translator(from_lang = lang_from, to_lang = lang_to)
#        translation = translator.translate(text)
#        return translation
#    except:
#        return "We are unable to process your request. Please try again in sometime"

    