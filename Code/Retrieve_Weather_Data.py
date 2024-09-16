import requests, json

#ToDo: save API key securely
API_KEY = #...

#ToDo: add long and lat to sqlite database
LATITUDE = 12
LONGITUDE = 50

url = f'https://api.openweathermap.org/data/2.5/weather?lat={LATITUDE}&lon={LONGITUDE}&appid={API_KEY}'

response = requests.get(url)
response = response.json()

BAD_REQUEST_ERROR_CODE = 400
API_KEY_ERROR_CODE = 401
LON_LAT_ERROR_CODE = 404
TOO_MANY_REQUESTS_ERROR_CODE = 429
INTERNAL_ERROR_CODE = '5xx'
CORRECT_REPONSE_CODE = 200

response_code = response['cod']

if response_code == CORRECT_REPONSE_CODE:
    print((response['weather'])[0]['description'])
else:
    print(response)