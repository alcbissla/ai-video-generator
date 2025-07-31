from PIL import Image, ImageDraw, ImageFont
import os

def generate_thumbnail(text):
    os.makedirs("static", exist_ok=True)
    img = Image.new('RGB', (720, 480), color=(0, 0, 0))
    d = ImageDraw.Draw(img)

    try:
        font = ImageFont.truetype("arial.ttf", 40)
    except:
        font = ImageFont.load_default()

    d.text((10, 200), text, fill=(255, 255, 255), font=font)
    img.save("static/thumbnail.png")
