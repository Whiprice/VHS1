from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import requests
import mysql.connector
import json
import os
from twilio.twiml.messaging_response import MessagingResponse
import openai

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

@app.route("/sms", methods=['GET','POST'])
def sms_reply():
    
    # Initialize the OpenAI API with your API key
    openai.api_key =  os.getenv("openaikey")

    # Get the incoming message from Twilio
    incoming_message = request.values.get("Body", "").strip()

    # Use the incoming message as the input to ChatGPT
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=f"{incoming_message}\n:",
        max_tokens=4000,  # Adjust the max tokens as needed
    )

    # Extract the AI's response from the API response
    ai_response = response.choices[0].text.strip()

    # Create a Twilio response with the AI's response
    twilio_resp = MessagingResponse()
    twilio_resp.message(ai_response)
    #resp = MessagingResponse()
    #resp.message("The robots are coming, head for the hills!")
    #return str(resp)

    return str(twilio_resp)

@app.route('/freeversion',methods=["GET", "POST"])
def freeversion():

    return render_template('freeversion.html')

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory('audio', filename)

@app.route('/athenapro',methods=["GET", "POST"])
def paidversion():
    return render_template('athenapro.html')

if __name__ == '__main__':    
    app.run(debug=True)
