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
    
    #Searching a for an entity in the table <<table_name>> based on conditions
    def search_table(self,what, table_name,search_condition,order_condition,limit_condition,foreign_key_condition):
            search_statement = f'SELECT {what} FROM {table_name} '
            if search_condition:
                search_statement=search_statement+ f'{foreign_key_condition} '
            if search_condition:
                search_statement=search_statement+ f'WHERE {search_condition} '
            if order_condition:
                search_statement=search_statement+ f'ORDER BY {order_condition} '
            if limit_condition:
                search_statement=search_statement+ f'LIMIT {limit_condition} '

            self.c.execute(search_statement)
            entities = self.c.fetchall()
            return(entities)
 
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


def return_five_most_recent():
    #open the database made in <<Initiate_Database.py>> 
    #had to be done in same thread as opening database
    DATABASE_NAME = 'RA2_Project_Database'
    active_database = SQLiteDatabase(DATABASE_NAME)
        
    CITIES_TABLE_NAME = 'Preset_Cities_Table'
    REQUEST_CITY_ID_COLUMN_NAME = 'city_id'
    CITY_ID_COLUMN_NAME = 'city_id'
    WEATHER_REQUEST_TABLE_NAME = 'Weather_Request_Log_Table'
    SEARCH_RETURN_CATEGORIES = 'timestamp, Weather_Summary, city_name'
    WHERE_CONDITION = 'response_status="success"'
    ORDER_CONDITION = 'timestamp DESC'
    LIMIT_CONDITION = 5
    FOREIGN_KEY_CONDITION = f'INNER JOIN {CITIES_TABLE_NAME} ON {CITIES_TABLE_NAME}.{CITY_ID_COLUMN_NAME} = {WEATHER_REQUEST_TABLE_NAME}.{REQUEST_CITY_ID_COLUMN_NAME}'
    five_most_recent = str(active_database.search_table(SEARCH_RETURN_CATEGORIES,WEATHER_REQUEST_TABLE_NAME,WHERE_CONDITION,ORDER_CONDITION,LIMIT_CONDITION,FOREIGN_KEY_CONDITION))
    active_database.close_database()
    return(five_most_recent)


def add_search_to_database(response,city_id,summary):
    #open the database made in <<Initiate_Database.py>> 
    #had to be done in same thread as opening database
    WEATHER_REQUEST_TABLE_NAME = 'Weather_Request_Log_Table'
    DATABASE_NAME = 'RA2_Project_Database'
    REQUEST_RESPONSE_STATUS_COLUMN_NAME = 'response_status'
    REQUEST_CITY_ID_COLUMN_NAME = 'city_id'
    REQUEST_SUMMARY_COLUMN_NAME = 'weather_summary'

    active_database = SQLiteDatabase(DATABASE_NAME)
    active_database.add_entity(WEATHER_REQUEST_TABLE_NAME,f'{REQUEST_RESPONSE_STATUS_COLUMN_NAME}, {REQUEST_CITY_ID_COLUMN_NAME}, {REQUEST_SUMMARY_COLUMN_NAME}',f'"{response}",{city_id},"{summary}"')
    active_database.close_database()


