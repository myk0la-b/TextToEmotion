from dotenv import load_dotenv
import os, codecs, json

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

for word in words:
    found = False
    for emotion_class in emotion_classes:
        if word in emotion_classes[emotion_class]:
            print(emotion_class)
            found = True
            break
    if not found:
        print("Incorrect!")
