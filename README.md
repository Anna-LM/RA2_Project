# RA2_Interview_Project
RA2 Technical Interview Coding Challenge Solution

Dependencies: 
    from flask import Flask, request
    from werkzeug.exceptions import HTTPException
    import sqlite3
    import requests


Use Initiate_Database.py the first time you use this code to create the database and populate city information

To start API:
    run -> main.py (python main.py)
    go to -> http://127.0.0.1:5000 (I used postman to check endpoints)
    Note: you need to change line 11 in <<main.py>> to your own API_KEY from open weather https://openweathermap.org/api

Endpoints:
    http://127.0.0.1:5000/history
    http://127.0.0.1:5000/weather
        argument: city_id

Error Handling:
    I have applied error handling throughout the api, including at the endpoints, the weather API and the database access. 


Database Schema:
    ER Diagram.png

Project Structure:
    RA2_Interview_Project
    |- Code
        |-Initiate_Database.py 
        |-Retrieve_Weather_Data.py 
        |-main.py 
        |-SQLite_Database.py 
    |- ER Diagram.png
    |- RA2_Project_Database.db
    |-ReadMe.md
    |-tests.py
    |-RA2 Python Developer Coding Challenge.pdf

Trade-Offs:
    I used flask over fast api since i have more experience with flask
    I chose SQLite over PostgreSQL since i have more experience with SQLite
    I tried to separate the functionalities into different files but due to threading issues i had to combine some functions into a file

Improvements:
    -> Docker File
    -> More detailed error responses
    -> UI/HTML
    -> Separate Dictionaries/Database handling from main code; ran into threading issue
    -> better stored API Key


