import os

import gtts
from playsound3 import playsound


def convert_text_to_speech(text):
    tts = gtts.gTTS(text, lang='en')  # Replace 'en' with your desired language code
    filename = 'output.mp3'  # Specify the output filename
    tts.save(filename)

    # Play the generated audio
    playsound(filename)
    os.remove(filename)


convert_text_to_speech("Hello World")
