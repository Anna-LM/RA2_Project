from flask import Flask, request

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


app.run()