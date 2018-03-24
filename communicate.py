from flask import Flask, request, jsonify
import MySQLdb
from serveraccess import value

app = Flask(__name__)

db = MySQLdb.connect("localhost", "root", value(), "trash")

#users
@app.route("/users/<id>", methods=['GET','POST'])
def user(id):
    if request.method=='POST':
        pass
    else:
        try:
            cursor = db.cursor()
            print("Hello")
            cursor.execute("SELECT * FROM USERS WHERE ID = %s" % str(id))
            print(" there!")
            result = cursor.fetchall()
            print(result)
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

@app.route("/users/get_all_users", methods=['GET', 'POST'])
def get_all_users():
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
@app.route("/bins/<bin_id>", methods=['GET', 'POST'])
def bins(bin_id):
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

@app.route("/bins/get_all_bins", methods=['GET', 'POST'])
def get_all_bins():
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
@app.route("/promotions/<promotions_id>", methods=['GET', 'POST'])
def promotions(promotions_id):
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

@app.route("/promotions/get_all_promotions", methods=['GET', 'POST'])
def get_all_promotions():
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
