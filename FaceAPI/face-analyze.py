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
    headers = {'Content-Type': 'application/octet-stream',
               'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceRectangle':"false",
        'returnFaceId': 'true',
        'returnFaceAttributes': 'age,gender,smile,glasses,emotion'
    }

    response = requests.post(face_api_url, params=params, headers=headers, data=image_data)
    response.raise_for_status()
    faces = response.json()
    print(faces)


if __name__ == '__main__':
    analyze()
