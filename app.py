from flask import Flask, request, url_for, render_template, jsonify
import requests
import os
import google.generativeai as genai


app = Flask(__name__)
model = genai.GenerativeModel("gemini-2.5-flash")
GEMINI_API_URL = "AIzaSyCx6yXtGV6XMlTb4WgF6gsyQtU6A3V732A"
api = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_URL)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/botchat", methods=["POST", "GET"])
def chat():
    userint = request.json.get("message")

    botResponse = model.generate_content(userint)
    reply = {"response": botResponse.text}
    return jsonify(reply)


if __name__ == "__main__":
    app.run(debug=True)
