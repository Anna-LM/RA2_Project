# RA2_Interview_Project
RA2 Technical Interview Coding Challenge Solution

Dependencies: 
    from flask import Flask, request
    from werkzeug.exceptions import HTTPException
    import sqlite3
    import requests


Use Initiate_Database.py the first time you use this code to create the database and populate city information

To start API:
    run -> main.py
    go to -> http://127.0.0.1:5000

Endpoints:
    http://127.0.0.1:5000/history
    http://127.0.0.1:5000/weather
        argument: city_id
