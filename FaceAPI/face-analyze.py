import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, \
    OperationStatusType
import capturePhoto as capture
import confidentials.FaceAPIConfig as configurations

KEY, ENDPOINT = configurations.config()


def analyze():
    image_name = capture.capture()
    # print("img_name "+img_name)
    image_path = os.path.join(str(image_name))
    # print("imagePath is " + image_path)
    image_data = open(image_path, "rb")
    # print(str(image_data))
    face_api_url = ENDPOINT + 'face/v1.0/detect'
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': KEY}

    params = {
        'returnFaceRectangle': "false",
        'returnFaceId': 'true',
        'returnFaceAttributes': 'age,gender,smile,glasses,emotion'
    }

    response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
    response.raise_for_status()
    faces = response.json()
    # print(faces)
    # print("Desired File name: "+img_name[:-4])

    return image_name, faces


def make_json(image_name, face_attributes):
    print(image_name[:-4])
    file_name = image_name[:-4] + '.json'
    file1 = open(file_name, 'w+')
    file1.write(str(face_attributes))


def detect_faces():
    # Create an authenticated FaceClient.
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    single_image_name = "CapFrame.jpg"
    image_path = os.path.join(single_image_name)
    image_data = open(image_path, "rb")
    detected_faces = face_client.face.detect_with_stream(image_data)
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))

    # Display the detected face ID in the first single-face image.
    # Face IDs are used for comparison to faces (their IDs) detected in other images.
    print('Detected face ID from', single_image_name, ':')
    for face in detected_faces: print(face.face_id)
    print()

    # Save this ID for use in Find Similar
    first_image_face_ID = detected_faces[0].face_id
    print(str(first_image_face_ID))


def face_dictonary():
    # Detect a face in an image that contains a single face
    face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))
    single_face_image_url = 'https://raw.githubusercontent.com/Microsoft/Cognitive-Face-Windows/master/Data/detection1.jpg'
    single_image_name = os.path.basename(single_face_image_url)
    detected_faces = face_client.face.detect_with_url(url=single_face_image_url)
    if not detected_faces:
        raise Exception('No face detected from image {}'.format(single_image_name))

    # Convert width height to a point in a rectangle
    def get_rectangle(faceDictionary):
        rect = faceDictionary.face_rectangle
        left = rect.left
        top = rect.top
        right = left + rect.width
        bottom = top + rect.height

        return (left, top), (right, bottom)

    # Download the image from the url
    response = requests.get(single_face_image_url)
    img = Image.open(BytesIO(response.content))

    # For each face returned use the face rectangle and draw a red box.
    print('Drawing rectangle around face... see popup for results.')
    draw = ImageDraw.Draw(img)
    for face in detected_faces:
        draw.rectangle(get_rectangle(face), outline='red')
    # Display the image in the users default image browser.
    img.show()
    time.sleep(10)


if __name__ == '__main__':
    # img_name, faces = analyze()
    # make_json(img_name, faces)
    # detect_faces()
    face_dictonary()
