from moviepy.editor import TextClip, CompositeVideoClip, AudioFileClip
import os
import requests

def make_video(text, resolution=(720, 1280)):
    from elevenlabs import generate, set_api_key
    set_api_key(os.getenv("ELEVENLABS_API_KEY"))
    audio = generate(text, voice="Bella")
    with open("static/voice.mp3", "wb") as f:
        f.write(audio)

    txt_clip = TextClip(text, fontsize=50, color='white', size=resolution).set_duration(10)
    audio_clip = AudioFileClip("static/voice.mp3")
    video = CompositeVideoClip([txt_clip.set_position('center')]).set_audio(audio_clip)
    video.write_videofile("static/video.mp4", fps=24)