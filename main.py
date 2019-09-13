import random
import codecs
import json
import os

from dotenv import load_dotenv

load_dotenv()

db_path = os.getenv('DB_PATH')


def get_db(path: str):
    with codecs.open(path, 'utf-8', 'r') as file:
        text_ = file.read()
        db = json.loads(text_)
    return db


if __name__ == '__main__':
    pass

text = input("Input your text: ")

emotion_images = {"sadness": "sad_img", "happiness": "happy_img"}
emotion_classes = {
    "sadness": ['sad', 'bad', 'sadness'], "happiness": ['happy', 'good']
}

words = text.split(' ')

result_image = ''


def check_emotion():
    for word in words:
        for emotion_class in emotion_classes:
            if word in emotion_classes[emotion_class]:
                return emotion_class


def emotion_to_image(em_class):
    rand_img = random.randint(0, len(emotion_images[em_class]) - 1)

    emotion_image = emotion_images[em_class][rand_img]

    return emotion_image


if __name__ == '__main__':
    result = emotion_to_image(check_emotion())
    print(result)
