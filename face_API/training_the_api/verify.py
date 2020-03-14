import glob
import os
import sys
import time
import uuid
import capturePhoto as cp
from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import TrainingStatusType
from msrest.authentication import CognitiveServicesCredentials
import required.FaceAPIConfig as fc

PERSON_GROUP_ID = fc.PERSON_GROUP_ID()
KEY, ENDPOINT = fc.config()

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


# Group image for testing against
def verify_image(image_name):
    group_photo = image_name
    IMAGES_FOLDER = os.path.join(os.path.dirname(os.path.realpath(__file__)))
    # Get test image
    test_image_array = glob.glob(os.path.join(IMAGES_FOLDER, group_photo))
    image = open(test_image_array[0], 'r+b')

    # Detect faces
    face_ids = []
    faces = face_client.face.detect_with_stream(image)
    for face in faces:
        face_ids.append(face.face_id)

    print("face_ids:", face_ids)

    # Identify faces
    if len(face_ids) != 0:
        results = face_client.face.identify(face_ids, PERSON_GROUP_ID)
        print('Identifying faces in {}'.format(os.path.basename(image.name)))
        try:
            if not results:
                print(
                    'No person identified in the person group for faces from {}.'.format(os.path.basename(image.name)))
            for person in results:
                print('Person for face ID {} is identified in {} with a confidence of {}.'.format(person.face_id,
                                                                                                  os.path.basename(
                                                                                                      image.name),
                                                                                                  person.candidates[
                                                                                                      0].confidence))
        except:
            print("You are not Identified")
    else:
        print("Please stay steady, Don't try to fool me")
    pass


if __name__ == '__main__':
    cp.capture("piano")
    verify_image("piano.jpg")
