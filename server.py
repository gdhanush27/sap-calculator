from flask import Flask, render_template, request,redirect, jsonify
from ocr import extract_text_from_image
import mysql.connector

def sap(li,str):
    c=0
    for i in str.split():
        if i in li:
            return bool(1)
    return bool(0)

myconn = mysql.connector.connect(host = "localhost", user = "Dhanush",passwd = "ttpod123",database = "mysql")  
cur = myconn.cursor() 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def first():
    return render_template('login.html')

@app.route("/login", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    cur.execute(query, (username, password))
    user = cur.fetchone()
    if user:
        return render_template('index.html')
    else:
        return render_template("login.html", message="Invalid username or password")

@app.route('/result', methods=['POST'])
def result():
        image = request.files['image'].read()
        text = extract_text_from_image(image)
        paper=["PAPER","Paper","paper"]
        present=["Presentation","presentation","PRESENTATION"]
        kongu=["KONGU","Kongu","kongu"]
        sapp=0
        if sap(kongu,text):
            if sap(paper,text):
                sapp=10
            elif sap(present,text):
                sapp=10
            else:
                sapp=5

        return render_template("index1.html", message=str(sapp))

if __name__ == "__main__":
    app.run(host='0.0.0.0',port = 8090)