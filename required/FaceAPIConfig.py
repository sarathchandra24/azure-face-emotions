subscription_key = "__FACE_API_KEY__"  # DSFace API
face_api_url = '__FACE_API_URL__'

PERSON_GROUP_IDs = "eidiko-auth"


def config():
    # print("Call Config")
    return subscription_key, face_api_url


def PERSON_GROUP_ID():
    return PERSON_GROUP_IDs
