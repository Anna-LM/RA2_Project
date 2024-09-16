from SQLite_Database import SQLiteDatabase,return_five_most_recent
from Retrieve_Weather_Data import Get_Weather
from flask import Flask, request
from werkzeug.exceptions import HTTPException

#open the database made in <<Initiate_Database.py>> 
DATABASE_NAME = 'RA2_Project_Database'
active_database = SQLiteDatabase(DATABASE_NAME)
    
#ToDo: save API key securely
API_KEY = "123456"
LATITUDE = 12
LONGITUDE = 50

Get_Weather (API_KEY,LATITUDE,LONGITUDE)



app = Flask(__name__)

@app.route('/weather', methods=['GET'])#,'POST'])
def return_weather():
    city_id = request.args.get('city_id')
    if city_id:
        print(city_id)
    return "Weather in City ... " , 200

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


