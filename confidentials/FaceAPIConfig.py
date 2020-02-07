
subscription_key = "e6d69a567691449da845339320fed9e7" #DSFace API
face_api_url = 'https://face-record-the-expressions.cognitiveservices.azure.com/face/v1.0/detect'


def config():
    print("Call Config")
    return subscription_key, face_api_url
