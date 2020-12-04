
"""Detects faces in an image."""
import os

from google.cloud import vision
import io

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'manifest-life-297521-49f580d85c9d.json'
client = vision.ImageAnnotatorClient()

file_name = 'faces.jpg'
image_path = r'C:\Users\Nozad\PycharmProjects\VisionAPI\images\faces.jpg'
with io.open(image_path, 'rb') as image_file:
    content = image_file.read()

image = vision.Image(content=content)

response = client.face_detection(image=image)
faces = response.face_annotations

# Names of likelihood from google.cloud.vision.enums
likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                   'LIKELY', 'VERY_LIKELY')
print('Faces:')

for face in faces:
    print('anger: {}'.format(likelihood_name[face.anger_likelihood]))
    print('joy: {}'.format(likelihood_name[face.joy_likelihood]))
    print('surprise: {}'.format(likelihood_name[face.surprise_likelihood]))

    vertices = (['({},{})'.format(vertex.x, vertex.y)
                for vertex in face.bounding_poly.vertices])

    print('face bounds: {}'.format(','.join(vertices)))

if response.error.message:
    raise Exception(
        '{}\nFor more info on error messages, check: '
        'https://cloud.google.com/apis/design/errors'.format(
            response.error.message))
