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


Database Schema:

Project Structure:

Trade-Offs:

Improvements:
    -> Docker File
    -> More detailed error responses
    -> UI/HTML
    -> Separate Dictionaries/Database handling from main code; ran into threading issue
    -> better stored API Key


