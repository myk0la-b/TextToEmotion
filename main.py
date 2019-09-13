text = input("Input your text: ")

emotion_images = {"sadness": "sad_img", "happiness": "happy_img"}
emotion_classes = {
"sadness": ['sad', 'bad'], "happiness": ['happy', 'good']
}

words = text.split(' ')

for word in words:
    for emotion_class in emotion_classes:
        if word in emotion_class:
            print (emotion_class)
        else:
            print("Incorrect!")
