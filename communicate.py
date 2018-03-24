from flask import Flask, request, jsonify
import MySQLdb
from serveraccess import value

app = Flask(__name__)

db = MySQLdb.connect("localhost", "root", value(), "trash")
cursor = db.cursor()

#users
@app.route("/user/<id>", methods=['GET','POST'])
def user(id):
    print("PRINT %s" % str(id))
    if request.method=='POST':
        pass
    else:
        try:
            cursor.execute("SELECT * FROM USERS WHERE ID = %s" % str(id))
            result = cursor.fetchall()
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

@app.route("/user/get_all_users", methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'POST':
        pass
    else:
        try:
            cursor.execute("SELECT * FROM USERS")
            result = cursor.fetchall()
            print(result)
            print(result)
            return jsonify(result)
        except:
            print("Error: unable to fetch data")

#bins
@app.route("/bins/<bin_id>", methods=['GET', 'POST'])
def bins(bin_id):
    print(bin_id)

    if request.method == 'POST':
        pass
    else:
        try:
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
            cursor.execute("SELECT * FROM PROMOTIONS")
            result = cursor.fetchall()
            return jsonify(result)
        except:
            print("Error: unable to fetch data")
