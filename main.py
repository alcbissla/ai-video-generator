from flask import Flask, request, send_file
from video_maker import make_video
from thumbnail_generator import generate_thumbnail
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route("/")
def home():
    return "AI Video Generator is running!"

@app.route("/generate", methods=["POST"])
def generate():
    data = request.get_json()
    text = data.get("text", "This is a default AI-generated video.")
    make_video(text)
    generate_thumbnail(text)
    return {"message": "Video and thumbnail generated!"}

@app.route("/video")
def get_video():
    return send_file("static/video.mp4", mimetype="video/mp4")

@app.route("/thumbnail")
def get_thumbnail():
    return send_file("static/thumbnail.png", mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
