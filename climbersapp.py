import os
import sys
import json
import sqlite3
from climber import Climber
from mountain import Mountain
from expedition import Expedition

#get expeditions info in table
def expeditions():
    with open("expeditions.json") as f:
        data = json.load(f)
        selfMountainID = 1
        for line in data:
            ID = line["id"]
            name = line["name"]
            start_location = line["start"]
            date = line["date"]
            country = line["country"]
            duration = line["duration"]
            succes = line["success"]

            conn = sqlite3.connect("climbersapp.db")
            c = conn.cursor()
            query = "INSERT or IGNORE INTO expeditions VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
            val = (ID,name,selfMountainID,start_location,date,country,duration,succes)
            c.execute(query, val)
            conn.commit()
            selfMountainID += 1

#data van climbers
def climbers():
    with open("expeditions.json") as f:
        data = json.load(f)
        for line in data:
            for climber in line["climbers"]:
                ID = int(climber["id"])
                first_name =  climber["first_name"]
                last_name = climber["last_name"]
                nationality = climber["nationality"]
                date_of_birth = climber["date_of_birth"]

                conn = sqlite3.connect("climbersapp.db")
                c = conn.cursor()
                query = "INSERT or IGNORE INTO climbers VALUES (?, ?, ?, ?, ?)"
                val = (ID, first_name, last_name, nationality, date_of_birth)
                c.execute(query, val)
                conn.commit()

def expedition_climbers():
    with open("expeditions.json") as f:
        data = json.load(f)
        conn = sqlite3.connect("climbersapp.db")
        c = conn.cursor()
        query = "INSERT or IGNORE INTO expedition_climbers VALUES (?, ?)"

        for line in data:
            for climber in line["climbers"]:
                climber_id = climber["id"]
                ID = line["id"]
                val = (climber_id, ID)
                c.execute(query, val)
        conn.commit()

def mountains():
    with open("expeditions.json") as f:
        data = json.load(f)
        selfMountainID = 1
        for line in data:
            name = line["mountain"]["name"]
            rank = line["mountain"]["rank"]
            range = line["mountain"]["range"]
            prominence = line["mountain"]["prominence"]
            height = line["mountain"]["height"]
            country = line["country"]
            conn = sqlite3.connect("climbersapp.db")
            c = conn.cursor()
            query = "INSERT or IGNORE INTO mountains VALUES (?, ?, ?, ?, ?, ?, ?)"
            val = (selfMountainID, name, country, rank, height, prominence, range)
            c.execute(query, val)
            conn.commit()
            selfMountainID += 1

def show_table_expeditions():
    conn = sqlite3.connect("climbersapp.db")
    c = conn.cursor()
    c.execute("SELECT * FROM expeditions")
    myresult = c.fetchall()
    for x in myresult:
        print(x)

def show_table_expedition_climbers():
    conn = sqlite3.connect("climbersapp.db")
    c = conn.cursor()
    c.execute("SELECT * FROM expedition_climbers")
    myresult = c.fetchall()
    for x in myresult:
        print(x)

def show_table_climbers():
    conn = sqlite3.connect("climbersapp.db")
    c = conn.cursor()
    c.execute("SELECT * FROM climbers")
    myresult = c.fetchall()
    for x in myresult:
        print(x)

def show_table_mountain():
    conn = sqlite3.connect("climbersapp.db")
    c = conn.cursor()
    c.execute("SELECT * FROM mountains")
    myresult = c.fetchall()
    for x in myresult:
        print(x)

def main():
    expeditions()
    mountains()
    climbers()
    expedition_climbers()

if __name__ == "__main__":
    main()
