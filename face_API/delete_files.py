import os

def make_blank(img_name):
    return
def delete_files(name):
    img_name=name[:-4]
    # os.remove(img_name + ".jpg")

    os.remove(img_name + ".json")
