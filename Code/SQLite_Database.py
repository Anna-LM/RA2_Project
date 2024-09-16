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
