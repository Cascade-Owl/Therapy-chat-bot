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


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/botchat", methods=["POST", "GET"])
def chat():
    userint = request.json.get("message")

    botResponse = model.generate_content(
        f"You are a comedic and cultured therapist, user says: {userint}"
    )
    reply = {"response": botResponse.text}
    return jsonify(reply)


if __name__ == "__main__":
    app.run(debug=True)
