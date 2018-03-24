from flask import Flask, request, jsonify
import MySQLdb
from serveraccess import value
import json
from decimal import Decimal
import constants

USER_KEYS = ['id', 'username', 'age', 'address', 'points']
BIN_KEYS = ['id', 'lat', 'lon', 'name', 'description', 'max_weight', 'current_weight']
PROMOTION_KEYS = ['id', 'multiplier', 'date_start', 'date_end', 'bin_id']


app = Flask(__name__)

db = MySQLdb.connect("localhost", "root", value(), "trash")

#users
@app.route("/user/<id>", methods=['GET','POST'])
def user(id):
    if request.method == 'POST':
        pass
    else:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM USERS WHERE ID = %s" % str(id))
            result = cursor.fetchall()
            print(result)

            all_users = []

            for user in result:
                tmpUser = {
                    "name": user[0],
                    "username": user[1],
                    "age": user[2],
                    "address": user[3],
                    "points": user[4]
                }

                all_users.append(tmpUser)

            #print(result)
            #json = jsonify(result)
            #print(result[0])
            return jsonify(all_users)
        except:
            print("Error: unable to fetch data")

    return "failed"

@app.route("/users", methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        pass
    else:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM USERS")
            result = cursor.fetchall()
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

#bins
@app.route("/bin/<bin_id>", methods=['GET', 'POST'])
def bin(bin_id):
    if request.method == 'POST':
        pass
    else:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM BINS WHERE ID = %s" % str(bin_id))
            result = cursor.fetchall()
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

@app.route("/bins", methods=['GET', 'POST'])
def bins():
    if request.method == 'POST':
        pass
    else:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM BINS")
            result = cursor.fetchall()
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

#lures
@app.route("/promotion/<promotions_id>", methods=['GET', 'POST'])
def promotion(promotions_id):
    if request.method == 'POST':
        pass
    else:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM PROMOTIONS WHERE ID = %s" % str(promotions_id))
            result = cursor.fetchall()
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

@app.route("/promotions", methods=['GET', 'POST'])
def promotions():
    if request.method == 'POST':
        pass
    else:
        try:
            cursor = db.cursor()
            cursor.execute("SELECT * FROM PROMOTIONS")
            result = cursor.fetchall()
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

def get_nearest_bin(my_location):
    if request.method == 'POST':
        pass
    else:
        try:
            my_lat = location.lat
            my_lon = location.lon
            cursor = db.cursor()
            cursor.execute("SELECT * FROM BINS")
            result = cursor.fetchall()

            # iterate through and find the bin the shortest distance away
            index = 0
            for bin in result:
                bin_lat = bin.lat
                bin_lon = bin.lon
                distance = haversine(my_lon, my_lat, bin_lon, bin_lat)
                if index == 0:
                    max_distance = distance
                    max_distance_index = 0
                else:
                    if distance < max_distance:
                        max_distance = distance
                        max_distance_index = index
                index += 1

            return jsonify(result[max_distance_index])

        except:
            print("Error: unable to fetch data")

# Taken from user Michael Dunn in his Stack Overflow response at this address:
# https://stackoverflow.com/questions/4913349/haversine-formula-in-python-bearing-and-distance-between-two-gps-points
def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371 # Radius of earth in kilometers. Use 3956 for miles
    return c * r
