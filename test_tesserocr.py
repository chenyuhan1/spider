import tesserocr
from PIL import Image
image = Image.open("D://images.png")
print(tesserocr.image_to_text(image))