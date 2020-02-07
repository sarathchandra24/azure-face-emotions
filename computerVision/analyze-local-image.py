import requests
import os
import sys
# If you are using a Jupyter notebook, uncomment the following line.
# %matplotlib inline
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO

# Add your Computer Vision subscription key and endpoint to your environment variables.

#for linux
#export COMPUTER_VISION_SUBSCRIPTION_KEY='d68bc65cbdf747c0bb18f95b2d1a0814'
#export COMPUTER_VISION_ENDPOINT = 'https://computer-vision-eidiko.cognitiveservices.azure.com/'

#for windows
#setx COMPUTER_VISION_SUBSCRIPTION_KEY 'd68bc65cbdf747c0bb18f95b2d1a0814'
#setx COMPUTER_VISION_ENDPOINT 'https://computer-vision-eidiko.cognitiveservices.azure.com/'
#
# if 'COMPUTER_VISION_SUBSCRIPTION_KEY' in os.environ:
#     subscription_key = os.environ['COMPUTER_VISION_SUBSCRIPTION_KEY']
# else:
#     print("\nSet the COMPUTER_VISION_SUBSCRIPTION_KEY environment variable.\n**Restart your shell or IDE for changes to take effect.**")
#     sys.exit()
#
# if 'COMPUTER_VISION_ENDPOINT' in os.environ:
#     endpoint = os.environ['COMPUTER_VISION_ENDPOINT']

endpoint="https://computer-vision-eidiko.cognitiveservices.azure.com/"

analyze_url = endpoint + "vision/v2.1/analyze"
subscription_key = "d68bc65cbdf747c0bb18f95b2d1a0814"
# Set image_path to the local path of an image that you want to analyze.
image_path = "ToGetAttributes.jpg"

# Read the image into a byte array
image_data = open(image_path, "rb").read()
headers = {'Ocp-Apim-Subscription-Key': subscription_key,
           'Content-Type': 'application/octet-stream'}
params = {'visualFeatures': 'Categories,Description,Color'}
response = requests.post(
    analyze_url, headers=headers, params=params, data=image_data)
response.raise_for_status()

# The 'analysis' object contains various fields that describe the image. The most
# relevant caption for the image is obtained from the 'description' property.
analysis = response.json()
print(analysis)
image_caption = analysis["description"]["captions"][0]["text"].capitalize()

# Display the image and overlay it with the caption.
image = Image.open(BytesIO(image_data))
plt.imshow(image)
plt.axis("off")
_ = plt.title(image_caption, size="x-large", y=-0.1)