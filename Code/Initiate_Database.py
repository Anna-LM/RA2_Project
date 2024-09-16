import sqlite3
from SQLite_Database import SQLiteDatabase

DATABASE_NAME = 'RA2_Project_Database'

# --- City Table ---
CITIES_TABLE_NAME = 'Preset_Cities_Table'

CITY_ID_COLUMN_NAME = 'city_id'
CITY_ID_TYPE = 'INTEGER'
CITY_ID_KEY  = 'PRIMARY KEY'
CITY_ID_COLUMN_INFORMATION = CITY_ID_COLUMN_NAME +' '+CITY_ID_TYPE+ ' '+CITY_ID_KEY
 
CITY_NAME_COLUMN_NAME = 'city_name'
CITY_NAME_TYPE = 'TEXT'
CITY_NAME_KEY  = 'UNIQUE'
CITY_NAME_COLUMN_INFORMATION = CITY_NAME_COLUMN_NAME +' '+CITY_NAME_TYPE+ ' '+CITY_NAME_KEY
 
CITY_LONGITUDE_COLUMN_NAME = 'city_longitude'
CITY_LONGITUDE_TYPE = 'REAL'
CITY_LONGITUDE_COLUMN_INFORMATION = CITY_LONGITUDE_COLUMN_NAME +' '+CITY_LONGITUDE_TYPE

CITY_LATITUDE_COLUMN_NAME = 'city_latitude'
CITY_LATITUDE_TYPE = 'REAL'
CITY_LATITUDE_COLUMN_INFORMATION = CITY_LATITUDE_COLUMN_NAME +' '+CITY_LATITUDE_TYPE
 
CITIES_TABLE_COLUMNS = CITY_ID_COLUMN_INFORMATION+', '+CITY_NAME_COLUMN_INFORMATION+', '+ CITY_LONGITUDE_COLUMN_INFORMATION+', '+CITY_LATITUDE_COLUMN_INFORMATION

CITIES=['Vancouver','Toronto','Quebec','Winnipeg','Calgary','Edmonton','Victoria','Saskatoon']

CITIES_DICTIONARY = {
    "Vancouver" : {
        "LONGITUDE" : 123.1207,
        "LATITUDE" : 49.2827
    },
    "Quebec" : {
        "LONGITUDE" : 71.2075,
        "LATITUDE" : 46.8131
    },
    "Toronto" : {
        "LONGITUDE" :79.3832,
        "LATITUDE" : 43.6532
    },
    "Winnipeg" : {
        "LONGITUDE" : 97.1385,
        "LATITUDE" : 49.8954
    },
    "Calgary" : {
        "LONGITUDE" : 114.0719,
        "LATITUDE" : 51.0447
    },
    "Edmonton" : {
        "LONGITUDE" : 113.4937,
        "LATITUDE" : 53.5461
    }
}

#Creating the database <<DATABASE_NAME>> 
active_database = SQLiteDatabase(DATABASE_NAME)
#Create a table of preset cities with at least city_id and city_name
active_database.create_table(CITIES_TABLE_NAME,CITIES_TABLE_COLUMNS)

#Adding the cities as entities in the database
for city in CITIES_DICTIONARY:
    active_database.add_entity(CITIES_TABLE_NAME,f'{CITY_NAME_COLUMN_NAME},{CITY_LONGITUDE_COLUMN_NAME},{CITY_LATITUDE_COLUMN_NAME}',f"'{city}','{CITIES_DICTIONARY[city]['LONGITUDE']}','{CITIES_DICTIONARY[city]['LATITUDE']}'")


# --- Weather Response Table ---
WEATHER_REQUEST_TABLE_NAME = 'Weather_Request_Log_Table'

REQUEST_ID_COLUMN_NAME = 'request_id'
REQUEST_ID_TYPE = 'INTEGER'
REQUEST_ID_KEY  = 'PRIMARY KEY'
REQUEST_ID_COLUMN_INFORMATION = REQUEST_ID_COLUMN_NAME +' '+REQUEST_ID_TYPE+ ' '+REQUEST_ID_KEY
 
REQUEST_CITY_ID_COLUMN_NAME = 'city_id'
REQUEST_CITY_ID_TYPE = 'INTEGER'
REQUEST_CITY_ID_KEY  = f'FOREIGN KEY ({REQUEST_CITY_ID_COLUMN_NAME}) REFERENCES {CITIES_TABLE_NAME} ({CITY_ID_COLUMN_NAME})'
REQUEST_CITY_ID_COLUMN_INFORMATION = REQUEST_CITY_ID_COLUMN_NAME +' '+REQUEST_CITY_ID_TYPE+ ', '+REQUEST_CITY_ID_KEY

REQUEST_RESPONSE_STATUS_COLUMN_NAME = 'response_status'
REQUEST_RESPONSE_STATUS_TYPE = 'TEXT'
REQUEST_RESPONSE_STATUS_COLUMN_INFORMATION = REQUEST_RESPONSE_STATUS_COLUMN_NAME +' '+REQUEST_RESPONSE_STATUS_TYPE

REQUEST_TIMESTAMP_COLUMN_NAME = 'timestamp'
REQUEST_TIMESTAMP_TYPE = 'TEXT'
REQUEST_TIMESTAMP_PROPERTIES='DEFAULT CURRENT_TIMESTAMP'
REQUEST_TIMESTAMP_COLUMN_INFORMATION = REQUEST_TIMESTAMP_COLUMN_NAME +' '+REQUEST_TIMESTAMP_TYPE+' '+REQUEST_TIMESTAMP_PROPERTIES

REQUEST_SUMMARY_COLUMN_NAME = 'weather_summary'
REQUEST_SUMMARY_TYPE = 'TEXT'
REQUEST_SUMMARY_COLUMN_INFORMATION = REQUEST_SUMMARY_COLUMN_NAME +' '+REQUEST_SUMMARY_TYPE

REQUESTS_TABLE_COLUMNS = REQUEST_ID_COLUMN_INFORMATION+', '+REQUEST_RESPONSE_STATUS_COLUMN_INFORMATION +', '+REQUEST_TIMESTAMP_COLUMN_INFORMATION +', '+REQUEST_SUMMARY_COLUMN_INFORMATION +', '+REQUEST_CITY_ID_COLUMN_INFORMATION


#A table for logging weather request
#Log each weather request in a database table, including at minimum: 
#    timestamp, requested city_id, and the response status (success/failure)
active_database.create_table(WEATHER_REQUEST_TABLE_NAME,REQUESTS_TABLE_COLUMNS)

DUMMY_RESPONSES=['success','failure','success']
DUMMY_CITY_IDS=[2,3,1]
DUMMY_SUMMARIES=['sunny','windy','cloudy']

for index in range (0,len(DUMMY_RESPONSES)):
    active_database.add_entity(WEATHER_REQUEST_TABLE_NAME,f'{REQUEST_RESPONSE_STATUS_COLUMN_NAME}, {REQUEST_CITY_ID_COLUMN_NAME}, {REQUEST_SUMMARY_COLUMN_NAME}',f'"{DUMMY_RESPONSES[index]}",{DUMMY_CITY_IDS[index]},"{DUMMY_SUMMARIES[index]}"')



#Create a history endpoint that returns data for the 5 most recent successful 
#    requests to the weather endpoint. Include the timestamp, city name, and 
#    a summary of the weather data returned for each request.
    
SEARCH_RETURN_CATEGORIES = 'timestamp, Weather_Summary, city_name'
WHERE_CONDITION = 'response_status="success"'
ORDER_CONDITION = 'timestamp DESC'
LIMIT_CONDITION = 5
FOREIGN_KEY_CONDITION = f'INNER JOIN {CITIES_TABLE_NAME} ON {CITIES_TABLE_NAME}.{CITY_ID_COLUMN_NAME} = {WEATHER_REQUEST_TABLE_NAME}.{REQUEST_CITY_ID_COLUMN_NAME}'

active_database.search_table(SEARCH_RETURN_CATEGORIES,WEATHER_REQUEST_TABLE_NAME,WHERE_CONDITION,ORDER_CONDITION,LIMIT_CONDITION,FOREIGN_KEY_CONDITION)

active_database.close_database()