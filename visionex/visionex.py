#set GOOGLE_APPLICATION_CREDENTIALS = 'c824a8ef45ebede1cbc8a528819a8b3247cb4a7b	'
import io
import os

def implicit():
    from google.cloud import storage

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

#DISCOVERY_URL = 'https://{api}.googleapis.com/$discovery/rest?version={apiVersion}'  # noqa
#BATCH_SIZE = 10

# Instantiates a client
vision_client = vision.Client('apikey.json')
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
#file_name = 'glucophage.png'
## detect remote image
# image = types.Image()
# image.source.image_uri = uri
## or local image
file_name = os.path.join(
    os.path.dirname(__file__),
    'glucophage.png')

# Loads the image into memory
with io.open(file_name,'rb') as image_file:
    content = image_file.read()
    #image = types.Image(content=content)
    image = vision_client.image(content=content)

#image = types.Image(content=content)

# Performs label detection on the image file
labels = image.detect_labels()
#response = client.label_detection(image=image)
#labels = response.label_annotations

#print('Labels:')
print('\nThis item is likely to be a:')
for label in labels:
    print(label.description)


# [START def_detect_logos]
def detect_logos(path):
    """Detects logos in the file."""
    #client = vision.ImageAnnotatorClient()

    # [START migration_logo_detection]
    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = types.Image(content=content)

    response = client.logo_detection(image=image)
    logos = response.logo_annotations
    print('\nBrand name is (if applicable):')

    for logo in logos:
        print(logo.description)
    # [END migration_logo_detection]
detect_logos('glucophage.png')


def detect_text(path):
    """Detects text in the file."""
    with io.open(path,'rb') as image_file:
        content = image_file.read()
# detect local image
    image = vision_client.image(content=content)

    texts = image.detect_text()


    #print('Texts:')
    print('\nThe writings on it say:')

    for text in texts:
        print('\n"{}"'.format(text.description))
## display text location in the image
        #vertices = (['({},{})'.format(bound.x_coordinate,bound.y_coordinate) for bound in text.bounds.vertices])
##OR
        #vertices = (['({},{})'.format(vertex.x, vertex.y)
                    #for vertex in text.bounding_poly.vertices])

        #print('bounds: {}'.format(','.join(vertices)))

detect_text('glucophage.png')