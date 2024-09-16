from SQLite_Database import SQLiteDatabase,return_five_most_recent,add_search_to_database
from Retrieve_Weather_Data import Get_Weather
from flask import Flask, request
from werkzeug.exceptions import HTTPException

#open the database made in <<Initiate_Database.py>> 
DATABASE_NAME = 'RA2_Project_Database'
active_database = SQLiteDatabase(DATABASE_NAME)

#ToDo: get key from other file
API_KEY="57ba810bdb5f5e12087fa6eb089ec8d9"


app = Flask(__name__)

#ToDo: Automate long/lat from database

@app.route('/weather', methods=['GET'])#,'POST'])
def return_weather():
    city_id = request.args.get('city_id')
    CITIES_DICTIONARY = {
            "1" : {
                "City_Name":'Vancouver',
                "LONGITUDE" : 123.1207,
                "LATITUDE" : 49.2827
            },
            "2" : {
                "City_Name":'Quebec',
                "LONGITUDE" : 71.2075,
                "LATITUDE" : 46.8131
            },
            "3" : {
                "City_Name":'Toronto',
                "LONGITUDE" :79.3832,
                "LATITUDE" : 43.6532
            },
            "4" : {
                "City_Name":'Winnipeg',
                "LONGITUDE" : 97.1385,
                "LATITUDE" : 49.8954
            },
            "5" : {
                "City_Name":'Calgary',
                "LONGITUDE" : 114.0719,
                "LATITUDE" : 51.0447
            },
            "6" : {
                "City_Name":'Edmonton',
                "LONGITUDE" : 113.4937,
                "LATITUDE" : 53.5461
            }
        }
    if city_id in CITIES_DICTIONARY:
        BAD_REQUEST_ERROR_CODE = 400
        API_KEY_ERROR_CODE = 401
        LON_LAT_ERROR_CODE = 404
        TOO_MANY_REQUESTS_ERROR_CODE = 429
        INTERNAL_ERROR_CODE = '5xx'
        CORRECT_REPONSE_CODE = 200
        
        RESPONSE_INDEX_CODE=0
        RESPONSE_INDEX_WEATHER_SUMMARY=1


        weather_api_response = Get_Weather(API_KEY,CITIES_DICTIONARY[city_id]['LATITUDE'],CITIES_DICTIONARY[city_id]['LONGITUDE'])
        ra2_api_response = None

        if weather_api_response[RESPONSE_INDEX_CODE]==CORRECT_REPONSE_CODE:
            add_search_to_database('success',city_id,weather_api_response[RESPONSE_INDEX_WEATHER_SUMMARY])
            ra2_api_response = f' Weather in {CITIES_DICTIONARY[city_id]} {weather_api_response[RESPONSE_INDEX_WEATHER_SUMMARY]}'
        else:   
            if weather_api_response[RESPONSE_INDEX_CODE]==BAD_REQUEST_ERROR_CODE:
                ra2_api_response = 'Bad Request'
            elif weather_api_response[RESPONSE_INDEX_CODE]==LON_LAT_ERROR_CODE:
                ra2_api_response = 'Lonitude/Latitude Error'
            elif weather_api_response[RESPONSE_INDEX_CODE]==TOO_MANY_REQUESTS_ERROR_CODE:
                ra2_api_response = 'Too Many Requests Error'
            elif weather_api_response[RESPONSE_INDEX_CODE]==API_KEY_ERROR_CODE:
                ra2_api_response = 'API Key Error'
            elif weather_api_response[RESPONSE_INDEX_CODE]==INTERNAL_ERROR_CODE:
                ra2_api_response = 'WEB API Error'      
            add_search_to_database('failure',city_id,'None')    

        return ra2_api_response , 200 
    else:
        #ToDo: improve this resposne
        ra2_api_response = 'Not in List of Cities choose 1:6'


        return ra2_api_response , 200

#ToDo: Make returned data more readable
@app.route('/history', methods=['GET'])
def return_history():
    return f"Most Recent searches:{return_five_most_recent()} " , 200

#Error Handling with Flask Endpoints
@app.errorhandler(HTTPException)
def handle_exception(e): 
    response = e.get_response()

    if e.code == 405:
        response = 'Please use GET request i.e. GET: http://127.0.0.1:5000/history, GET: http://127.0.0.1:5000/weather?city_id=1'
    elif e.code == 404:
        response = 'Please use weather or history endpoints i.e. GET: http://127.0.0.1:5000/history, GET: http://127.0.0.1:5000/weather?city_id=1'
    else:
        response = 'Unprecidented error, please try again i.e. GET: http://127.0.0.1:5000/history, GET: http://127.0.0.1:5000/weather?city_id=1'

    return response

app.run()


