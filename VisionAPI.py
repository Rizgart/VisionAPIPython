import io
import os

from google.cloud import vision, vision_v1
from google.cloud.vision_v1 import types
import pandas as pd

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'manifest-life-297521-49f580d85c9d.json'
client = vision.ImageAnnotatorClient()

file_name = 'text.jpg'
image_path = r'C:\Users\Nozad\PycharmProjects\VisionAPI\images\text.jpg'

with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

# construct an iamge instance
image = vision_v1.types.Image(content=content)

# annotate Image Response
response = client.text_detection(image=image)  # returns TextAnnotation
df = pd.DataFrame(columns=['locale', 'description'])

texts = response.text_annotations
for text in texts:
    df = df.append(
        dict(
            locale=text.locale,
            description=text.description
        ),
        ignore_index=True
    )

print(df['description'][0])
