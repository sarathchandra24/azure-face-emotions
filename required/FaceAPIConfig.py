subscription_key = "c0235fcc9d60470c8a39054f04a7c904"  # DSFace API
face_api_url = 'https://get-expressions.cognitiveservices.azure.com/'

PERSON_GROUP_IDs = "eidiko-auth"


def config():
    # print("Call Config")
    return subscription_key, face_api_url


def PERSON_GROUP_ID():
    return PERSON_GROUP_IDs
