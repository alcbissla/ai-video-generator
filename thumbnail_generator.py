from PIL import Image, ImageDraw, ImageFont
import os

def generate_thumbnail(text):
    os.makedirs("static", exist_ok=True)
    image = Image.new('RGB', (720, 1280), color=(73, 109, 137))
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text((10, 600), text, font=font, fill=(255, 255, 0))
    image.save("static/thumbnail.png")
