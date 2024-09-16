import sqlite3

#A class for initiating the database <<database_name>>
class SQLiteDatabase:
    #Opens the database <<database_name>>, creates the database if doesnt exist
    def __init__(self,database_name):
        self.conn = sqlite3.connect(f'{database_name}.db')
        self.c = self.conn.cursor()

    #Creating a table named <<table_name>> with columns <<table_columns_information>>
    def create_table(self,table_name,table_columns_information):
        self.c.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({table_columns_information})')
        self.conn.commit()
    
    #Searching a for an entity in the table <<table_name>> based on a condition
    def search_table(self,search_selection, table_name,search_condition):
        search_statement = f'SELECT {search_selection} FROM {table_name} '

        if search_condition:
            search_statement=search_statement+ f'WHERE {search_condition} '

        self.c.execute(search_statement)
        entities = self.c.fetchall()
        print(entities)
 
    #Adding entities/rows to the table <<table_name>>
    def add_entity(self,table_name,column,value):
        self.c.execute(f'INSERT OR IGNORE INTO {table_name} ({column}) VALUES ({value})')
        self.conn.commit()
    
    #Deleting entities form the table <<table_name>> based on a condition <<delete_condition>>
    def delete_entity(self,table_name,delete_condition):
        self.c.execute(f'DELETE FROM {table_name} WHERE {delete_condition}')
        self.conn.commit()

    #Closing the database, this must be done every time the database is accessed
    def close_database(self):
        self.conn.close()

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
 
CITIES_TABLE_COLUMNS = CITY_ID_COLUMN_INFORMATION+', '+CITY_NAME_COLUMN_INFORMATION

CITIES=['Vancouver','Toronto','Quebec','Winnipeg','Calgary','Edmonton','Victoria','Saskatoon']

#Creating the database <<DATABASE_NAME>> 
active_database = SQLiteDatabase(DATABASE_NAME)
#Create a table of preset cities with at least city_id and city_name
active_database.create_table(CITIES_TABLE_NAME,CITIES_TABLE_COLUMNS)

#Adding the cities as entities in the database
for city in CITIES:
    active_database.add_entity(CITIES_TABLE_NAME,CITY_NAME_COLUMN_NAME,f"'{city}'")


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

DUMMY_RESPONSES=['one','two','three']
DUMMY_CITY_IDS=[2,3,1]
DUMMY_SUMMARIES=['sunny','windy','cloudy']

for index in range (0,len(DUMMY_RESPONSES)):
    active_database.add_entity(WEATHER_REQUEST_TABLE_NAME,f'{REQUEST_RESPONSE_STATUS_COLUMN_NAME}, {REQUEST_CITY_ID_COLUMN_NAME}, {REQUEST_SUMMARY_COLUMN_NAME}',f'"{DUMMY_RESPONSES[index]}",{DUMMY_CITY_IDS[index]},"{DUMMY_SUMMARIES[index]}"')

