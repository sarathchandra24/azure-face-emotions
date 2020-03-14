import glob
import sys
import time
import uuid

from azure.cognitiveservices.vision.face import FaceClient
from azure.cognitiveservices.vision.face.models import TrainingStatusType
from msrest.authentication import CognitiveServicesCredentials

import required.FaceAPIConfig as fc

KEY, ENDPOINT = fc.config()

# Create an authenticated FaceClient.
face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

PERSON_GROUP_ID = 'eid-test1'

TARGET_PERSON_GROUP_ID = str(uuid.uuid4()) # assign a random ID (or name it anything)


def train():
    print("Person Group ID name:"+PERSON_GROUP_ID)

    print("TARGET_PERSON_GROUP_ID is :"+ TARGET_PERSON_GROUP_ID)

    print('Person group:', PERSON_GROUP_ID)

    # if you want to delete the pre existing Person group un comment the below line
    # face_client.person_group.delete(PERSON_GROUP_ID)

    face_client.person_group.create(person_group_id=PERSON_GROUP_ID, name=PERSON_GROUP_ID)

    # Define sarath
    sarath = face_client.person_group_person.create(PERSON_GROUP_ID, "sarath")
    print("sarath person group ID: ",sarath.person_id)
    # Define bandaru
    bandaru = face_client.person_group_person.create(PERSON_GROUP_ID, "bandaru")
    print("bandaru person group ID:" ,bandaru.person_id)

    # Find all jpeg images of friends in working directory
    sarath_images = [file for file in glob.glob('images\*.jpg') if file.startswith("sar")]
    bandaru_images = [file for file in glob.glob('images\*.jpg') if file.startswith("ban")]


    # Add to a sarath person
    for image in sarath_images:
        w = open(image, 'r+b')
        face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, sarath.person_id, w)

    # Add to a bandaru person
    for image in bandaru_images:
        m = open(image, 'r+b')
        face_client.person_group_person.add_face_from_stream(PERSON_GROUP_ID, bandaru.person_id, m)


    print()
    print('Training the person group...')
    # Train the person group
    face_client.person_group.train(PERSON_GROUP_ID)

    while True:
        training_status = face_client.person_group.get_training_status(PERSON_GROUP_ID)
        print("Training status: {}.".format(training_status.status))
        print()
        if training_status.status is TrainingStatusType.succeeded:
            print("Success Fully Trained")
            break
        elif training_status.status is TrainingStatusType.failed:
            sys.exit('Training the person group has failed.')
        time.sleep(5)

    pass


if __name__ == '__main__':
    train()