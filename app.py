from flask import Flask, render_template, request, redirect, url_for
import requests
import mysql.connector
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/collegeportal')
def projects():
    return render_template('SchoolSign.html')

@app.route('/studentportal')
def resume():
    return render_template('StudentSign.html')

@app.route('/thank_you')
def thank_you():
    return render_template('thankyou.html')

@app.route('/freeversion',methods=["GET", "POST"])
def freeversion():
    if request.method == "POST":
        # Get user input from the form
        db = mysql.connector.connect(
        username="doadmin",
        password="AVNS_iuOLTr_1rACvDK-o1Nl",
        host="athena-database-do-user-14760374-0.b.db.ondigitalocean.com",
        port=25060,
        database="defaultdb",
    #sslmode="REQUIRED"
        )
        cursor = db.cursor()
        name = request.form["name"]
        canvas_url = request.form["canvas_url"]
        api_token = request.form["api_token"]
        phone_number = request.form["phone_number"]
        
        # Insert the user data into the MySQL database
        query = "INSERT INTO athenalite2 (name, canvas_url, api_token, phone_number) VALUES (%s, %s, %s, %s)"
        values = (name, canvas_url, api_token, phone_number)
        cursor.execute(query, values)
        db.commit()
        # Close the database connection
        db.close()
        return render_template('thankyou.html')

        

    
    return render_template('freeversion.html')

@app.route('/athenapro',methods=["GET", "POST"])
def paidversion():
    return render_template('athenapro.html')

if __name__ == '__main__':    
    app.run(debug=True)

