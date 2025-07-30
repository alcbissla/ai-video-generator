import os
from PIL import Image
import requests
from io import BytesIO

def generate_thumbnail(text):
    from openai import OpenAI
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    response = openai.images.generate(prompt=text, n=1, size="512x512")
    image_url = response.data[0].url
    img_data = requests.get(image_url).content
    with open("static/thumbnail.png", "wb") as f:
        f.write(img_data)