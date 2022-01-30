from google.cloud import firestore
from flask import Blueprint, render_template, redirect, url_for, request, flash, session, abort, current_app
# read https://cloud.google.com/firestore/docs/quickstart-servers#firestore_setup_dataset_pt1-python

import os
# The `project` parameter is optional and represents which project the client
# will act on behalf of. If not supplied, the client falls back to the default
# project inferred from the environment.
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = os.path.abspath("firestore_keys.json")
db = firestore.Client(project='alien-segment-337020')

# upload an html file to firestore

def upload_image_to_firebase(image_file_path, email):
    # check if session exists
    with open(image_file_path, "rb") as image_file:
        file_name = os.path.basename(image_file_path)
        doc_ref = db.collection(u'users').document(u'{}'.format(email))
        doc_ref
        doc_ref.set({
            u'postcard_{}_data'.format(file_name): image_file.read(),
            u'postcard_{}_name'.format(file_name): file_name,
        }, merge=True)

#     return an html response that indicates the upload was successful
    return "upload successful"

upload_image_to_firebase(os.path.abspath('imgs/eiffel tower.jpg'), 'salvadoraleguas@gmail.com')
def get_image_from_firebase(image_name, email):
    # check if session exists

    doc_ref = db.collection(u'users').document(u'{}'.format(email))
    doc_ref.get().to_dict()
    file_name = image_name.split("_")[1]
    with open('imgs/{}'.format(file_name), "wb") as image_file:
        image_file.write(doc_ref.get().to_dict()[image_name])
    return 'imgs/{}'.format(file_name)
# upload_html_to_firestore("bucket.jpg")

# make a function that gets all the imagenames with email from firestore
def get_image_names_from_firebase(email):
    # check if session exists
    doc_ref = db.collection(u'users').document(u'{}'.format(email))
    dic = doc_ref.get().to_dict()
    # make a list of all the image names
    image_names = []
    for key in dic.keys():
        if "_name" in key:
            image_names.append(dic[key])
    return image_names
