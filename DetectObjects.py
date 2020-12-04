import io, os
from numpy import random
from google.cloud import vision
from Pillow_Utility import draw_border, Image
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"manifest-life-297521-49f580d85c9d.json"
client = vision.ImageAnnotatorClient()

file_name = 'ikea3.jpg'
image_path = os.path.join('.\Images', file_name)

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.types.Image(content=content)
response = client.object_localization(image=image)
localized_object_annotations = response.localized_object_annotations

pillow_image = Image.open(image_path)
df = pd.DataFrame(columns=['name', 'score'])
for obj in localized_object_annotations:
    df = df.append(
        dict(
            name=obj.name,
            score=obj.score
        ),
        ignore_index=True)

    r, g, b = random.randint(150, 255), random.randint(
        150, 255), random.randint(150, 255)

    draw_border(pillow_image, obj.bounding_poly, (r, g, b),
                 pillow_image.size, obj.name, obj.score)

print(df)
pillow_image.show()
