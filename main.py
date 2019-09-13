from pprint import pprint


text = input("Input your text: ")

emotion_images = {"sadness": "sad_img", "happiness": "happy_img"}
emotion_classes = {
    "sadness": ['sad', 'bad', 'sadness'], "happiness": ['happy', 'good']
}

words = text.split(' ')
pprint(words)

for word in words:
    found = False
    for emotion_class in emotion_classes:
        if word in emotion_classes[emotion_class]:
            print(emotion_class)
            found = True
            break
    if not found:
        print("Incorrect!")
