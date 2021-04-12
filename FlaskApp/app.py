from datetime import datetime
from flask import Flask, render_template, request, redirect, session, url_for
from pymongo import MongoClient

app = Flask(__name__)

@app.route("/Form", methods=['GET', 'POST'])
def Form():
    return render_template("form.html")


@app.route('/Home', methods=['GET', 'POST'])
def home():
    client = MongoClient(
        "mongodb+srv://FinalProject:1234@cluster0-lnafe.azure.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Agile
    collection = db.Home

    if request.method == "POST":
        req = request.form
        print(req)
        hrec = {
            "FirstName": req["fname"],
            "MiddleName": req["mname"],
            "LastName": req["lname"],
            "Cars": req["cars"],
            "Phone": req["Phone Number"],
            "Email": req["email"],
            "Address": req["Address"],
            "Years": req["years"],
            "Date": req["Date"],
            "Amount": req["Number"]
        }
        print(hrec)
        x = collection.insert_one(hrec)
        return redirect(url_for('homef'))
    return render_template('home.html')

@app.route('/Homef', methods=['GET', 'POST'])
def homef():
    return render_template('homef.html')

@app.route('/Car', methods=['GET', 'POST'])
def car():
    client = MongoClient(
        "mongodb+srv://FinalProject:1234@cluster0-lnafe.azure.mongodb.net/test?retryWrites=true&w=majority")
    db = client.Agile
    collection = db.Car

    if request.method == "POST":
        req = request.form
        print(req)
        carec = {
            "FirstName": req["fname"],
            "MiddleName": req["mname"],
            "LastName": req["lname"],
            "Phone": req["Phone Number"],
            "Email": req["email"]
        }
        x = collection.insert_one(carec)
        return redirect(url_for('carf'))
    return render_template('car.html')

@app.route('/Carf', methods=['GET', 'POST'])
def carf():
        return render_template('carf.html')

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == "POST":
        req = request.form
        print(req)
        if req["u"] == "ashish" and req["p"] == "1234":
            return redirect(url_for('Form'))
        else:
            return redirect(url_for('incorrect'))
    return render_template('index.html')

@app.route("/incorrect", methods=['GET', 'POST'])
def incorrect():
    if request.method == "POST":
        req = request.form
        print(req)
        if req["u"] == "ashish" and req["p"] == "1234":
            return redirect(url_for('Form'))
        else:
            return redirect(url_for('incorrect'))
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
