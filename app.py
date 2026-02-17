from flask import Flask, request, url_for, render_template, jsonify
from dotenv import load_dotenv
import requests
import os
import google.generativeai as genai

load_dotenv()

app = Flask(__name__)

GEMINI_API_URL = os.getenv("GEMINI_API_URL")
genai.configure(api_key=GEMINI_API_URL)
model = genai.GenerativeModel("gemini-2.5-flash")

chat_history=[]
chat_historybot=[]
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/botchat", methods=["POST", "GET"])
def chat():
    userint = request.json.get("message")



    botResponse = model.generate_content(
        f"""{chat_history}/n You are a slightly serious, professional speaking, yet comedic and a humourous therapist, 
        if someone prompts for another topic unrelated to your therapist job, 
        tell them that you are a therapist only, and you can't do other unrelated topic but be sensitive, user says: {userint}"""
    )
    reply = {"response": botResponse.text}
    chat_history.append({"role": "user", "parts": [str(userint)]})
    chat_historybot.append({"role": "model", "parts": [botResponse.text]})

    return jsonify(reply)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
