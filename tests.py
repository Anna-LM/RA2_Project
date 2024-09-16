import unittest
import requests
from Code.Retrieve_Weather_Data import Get_Weather




class TestWeathers(unittest.TestCase):


    def test_cities_that_exist(self):

        CITIES_DICTIONARY = {
            "1" : {
                "ID":1,
                "City_Name":'Vancouver',
                "LONGITUDE" : 123.1207,
                "LATITUDE" : 49.2827
            },
            "2" : {
                "ID":2,
                "City_Name":'Quebec',
                "LONGITUDE" : 71.2075,
                "LATITUDE" : 46.8131
            },
            "3" : {
                "ID":3,
                "City_Name":'Toronto',
                "LONGITUDE" :79.3832,
                "LATITUDE" : 43.6532
            },
            "4" : {
                "ID":4,
                "City_Name":'Winnipeg',
                "LONGITUDE" : 97.1385,
                "LATITUDE" : 49.8954
            },
            "5" : {
                "ID":5,
                "City_Name":'Calgary',
                "LONGITUDE" : 114.0719,
                "LATITUDE" : 51.0447
            },
            "6" : {
                "ID":6,
                "City_Name":'Edmonton',
                "LONGITUDE" : 113.4937,
                "LATITUDE" : 53.5461
            }
        }
        API_KEY = "123"
        
        for city in CITIES_DICTIONARY:  
            longitude = CITIES_DICTIONARY[city]['LONGITUDE']
            latitude = CITIES_DICTIONARY[city]['LATITUDE']
            city_index = CITIES_DICTIONARY[city]['ID']
            WEATHER_RESPONSE_INDEX = 1
            #reposne from weather api
            weather_api_response= Get_Weather(API_KEY,latitude,longitude)
            weather_api_reponse_conditions = weather_api_response[WEATHER_RESPONSE_INDEX]
            #response from my api
            my_api_response  = requests.get(f'http://127.0.0.1:5000/weather?city_id={city_index}')
            my_api_response = (my_api_response.text.split('} ')[1])
            #compare the two results
            self.assertEqual(weather_api_reponse_conditions, my_api_response)
            
    def test_cities_that_doesnt_exist(self):
        my_api_response  = requests.get(f'http://127.0.0.1:5000/weather?city_id={10}')
        correct_reponse = 'Not in List of Cities choose 1:6'
        self.assertEqual(correct_reponse, my_api_response.text)

    def test_no_city_weather_end_point(self):
        my_api_response  = requests.get(f'http://127.0.0.1:5000/weather')
        correct_reponse = 'Not in List of Cities choose 1:6'
        self.assertEqual(correct_reponse, my_api_response.text)
        
    def test_incorrect_endpoint(self):
        my_api_response  = requests.get(f'http://127.0.0.1:5000/abc')
        print(my_api_response.text)
        correct_reponse = 'Please use weather or history endpoints i.e. GET: http://127.0.0.1:5000/history, GET: http://127.0.0.1:5000/weather?city_id=1'
        self.assertEqual(correct_reponse, my_api_response.text)


    def test_post_not_get(self):
        my_api_response  = requests.post(f'http://127.0.0.1:5000/abc')
        correct_reponse = 'Please use weather or history endpoints i.e. GET: http://127.0.0.1:5000/history, GET: http://127.0.0.1:5000/weather?city_id=1'
        self.assertEqual(correct_reponse, my_api_response.text)

    #ToDo ... get from Database, test history endpoints
    #def test_history_correct(self):
    #    my_api_response  = requests.get(f'http://127.0.0.1:5000/history')
    #    print(my_api_response.text)
    #    correct_reponse = 'Please use weather or history endpoints i.e. GET: http://127.0.0.1:5000/history, GET: http://127.0.0.1:5000/weather?city_id=1'
    #    self.assertEqual(correct_reponse, my_api_response.text)



        
if __name__ == '__main__':
    unittest.main()
