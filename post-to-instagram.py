import os
from instagrapi import Client

def login_instagram():
    cl = Client()
    username = os.getenv("IG_USERNAME")
    password = os.getenv("IG_PASSWORD")
    cl.login(username, password)
    return cl

def post_image(image_path, caption):
    cl = login_instagram()
    cl.photo_upload(image_path, caption)
