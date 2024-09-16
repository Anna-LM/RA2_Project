from flask import Flask, request
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

@app.route('/weather', methods=['GET'])#,'POST'])
def return_weather():
    city_id = request.args.get('city_id')
    if city_id:
        print(city_id)
    return "Weather in City ... " , 200

@app.route('/history', methods=['GET'])
def return_history():
    return "Most Recent searches ... " , 200

#Error Handling with Flask Endpoints
#ToDo: add more detailed error messages
@app.errorhandler(HTTPException)
def handle_exception(e): 
    response = e.get_response()
    if e.code == 405:
        response = 'Please use Get'
    elif e.code == 404:
        response = 'Please use weather or history'
    else:
        response = 'Unprecidented error, please try again'

    return response

app.run()