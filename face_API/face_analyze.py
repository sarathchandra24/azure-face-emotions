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
import face_API.capturePhoto as capture
import required.FaceAPIConfig as configurations
import face_API.delete_files as df

KEY, ENDPOINT = configurations.config()


def analyze(img_name):
    image_name = img_name
    # image_name = capture.capture(img_name)
    # print("img_name "+image_name)
    image_path = os.path.join(str(image_name))
    # print("imagePath is " + image_path)
    image_data = open(image_path, "rb")
    # print(str(image_data))
    face_api_url = ENDPOINT + 'face/v1.0/detect'
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': KEY}

    params = {
        'returnFaceRectangle': "true",
        'returnFaceId': 'true',
        'returnFaceAttributes': 'age,gender,smile,glasses,emotion'
    }

    response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
    response.raise_for_status()
    faces_attribute = response.json()
    # print(faces_attribute)
    # print("Desired File name: "+image_name[:-4])
    # print("Sleeping in analyze")
    # time.sleep(5)
    return image_name, faces_attribute


def make_json(image_name, attributes):
    # print(image_name[:-4])
    file_name = image_name[:-4] + '.json'
    file1 = open(file_name, 'w+')
    file1.write(str(attributes))
    # print("sleeping in make _json")
    # time.sleep(5)
    pass


def show_rectangle(rect, image_name):
    def getRectangle(rectangle):
        left = rectangle['left']
        top = rectangle['top']
        right = left + rectangle['width']
        bottom = top + rectangle['height']

        return (left, top), (right, bottom)

    img = Image.open(image_name)
    draw = ImageDraw.Draw(img)
    draw.rectangle(getRectangle(rect), outline='red')
    img.save(image_name)
    # img.show()
    return True


def face_analyze(image_name):
    img_name, faces_attributes = analyze(image_name)
    print("face attributes")
    print(faces_attributes)
    print("length is", len(faces_attributes))
    try:
        print("length is", len(faces_attributes))
        for i in range(len(faces_attributes)):
            dict1 = faces_attributes[i]
            faceID = dict1['faceId']
            face_rectangle = dict1['faceRectangle']
            face_attributes = dict1['faceAttributes']
            make_json(img_name, faces_attributes)
            # time.sleep(10)
            # print("Image name in main",img_name)
            # print("faceID is",faceID)
            # print("face Rectangle",face_rectangle)
            # print("face attributes",face_attributes)
            show_rectangle(face_rectangle, img_name)
            # df.delete_files(img_name)

    except:
        print("per son not identified")


if __name__ == '__main__':
    face_analyze("C:/Users/Sarat/PycharmProjects/AzureFaceEmotions/face_API/temp_images/sar123.jpg")
