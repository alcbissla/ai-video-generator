from flask import Flask, send_file
from video_maker import make_video
from thumbnail_generator import generate_thumbnail

app = Flask(__name__)

@app.route('/generate')
def generate():
    script = "Welcome to the future of AI-generated videos!"
    make_video(script, resolution=(720, 1280))
    generate_thumbnail(script)
    return {"status": "Video and thumbnail generated!"}

@app.route('/video')
def video():
    return send_file('static/video.mp4', mimetype='video/mp4')

@app.route('/thumbnail')
def thumbnail():
    return send_file('static/thumbnail.png', mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)