import requests
from PIL import Image
import os
import capturePhoto as capture
import confidentials.FaceAPIConfig as cnfg

import sys


def analyze():
    img_name = capture.capture()
    # print("img_name "+img_name)
    image_path = os.path.join(str(img_name))
    # print("imagePath is " + image_path)
    image_data = open(image_path, "rb")
    # print(str(image_data))
    subscription_key, face_api_url = cnfg.config()
    face_api_url = face_api_url+'face/v1.0/detect'
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}

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

    return img_name, faces


def makeJson(img_name, faces, self):
    print(img_name[:-4])
    file_name = img_name[:-4] + '.json'
    file1 = open(file_name, 'w+')
    file1.write(str(faces))


if __name__ == '__main__':
    img_name, faces = analyze()
