from flask import Flask
from flask import render_template, request, jsonify
import requests
import random

app = Flask(__name__)
app.secret_key = '12345'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat',methods=['POST'])
def chat():
    try:
        user_message =  request.form['text']
        print (user_message)
        response = requests.get("http://localhost:5005/parse",params={"q":user_message})
        response = response.json()
        print (response)
        entities = response.get("entities")
        intent = response.get("intent")
        print("Intent {}, Entities {}".format(intent['name'],entities))
        return jsonify({"status":"success", "response":"Good boy"})
    except Exception as e:
        print("exception")
        print(e)
        return jsonify({"status":"success","response":"Sorry, IT Assistant is currently down..."})

app.config["DEBUG"] = True
if __name__ == "__main__":
    app.run(debug=True,port=8080)