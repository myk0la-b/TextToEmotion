import random
import codecs
import json
import os

from dotenv import load_dotenv

load_dotenv()

emotions_db_path = os.getenv('DB_PATH')
emotions_to_image_path = os.getenv('IMAGES_PATH')


def get_db(path: str):
    with codecs.open(path, encoding='utf-8', mode='r') as file:
        text_ = file.read()
        db = json.loads(text_)
    return db


def get_emotions_db():
    return get_db(emotions_db_path)


def get_emotion_to_image_db():
    return get_db(emotions_to_image_path)


if __name__ == '__main__':
    pass

text = input("Input your text: ")

# emotion_images = {"sadness": ['sad_img'], "happiness": ['happy_img', 'a', 'f', 'g', 's', 'h']}

words = text.split(' ')

result_image = ''


def check_emotion():
    emotion_classes = get_emotions_db()
    for word in words:
        for emotion_class in emotion_classes:
            if word in emotion_classes[emotion_class]:
                return emotion_class
    return None


def emotion_to_image(em_class):
    if em_class is None:
        return None
    emotion_images = get_emotion_to_image_db()
    rand_img = random.randint(0, len(emotion_images[em_class]) - 1)

    emotion_image = emotion_images[em_class][rand_img]

    return emotion_image


if __name__ == '__main__':
    result = emotion_to_image(check_emotion())
    print(result)
