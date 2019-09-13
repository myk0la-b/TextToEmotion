import random

text = input("Input your text: ")

emotion_images = {"sadness": ['sad_img'], "happiness": ['happy_img', 'a' , 'f', 'g', 's', 'h']}
emotion_classes = {
"sadness": ['sad', 'bad'], "happiness": ['happy', 'good']
}

words = text.split(' ')

result_image  = ''

def check_emotion():
    for word in words:
        for emotion_class in emotion_classes:
            if word in emotion_classes[emotion_class]:
                return emotion_class

def emotion_to_image(em_class):

    rand_img = random.randint(0, len(emotion_images[em_class])- 1)

    emotion_image = emotion_images[em_class][rand_img]

    return emotion_image

if __name__ == '__main__':
    result = emotion_to_image(check_emotion())
    print(result)
