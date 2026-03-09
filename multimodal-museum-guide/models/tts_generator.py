from gtts import gTTS
import os

def generate_audio(text,id):

    folder="static/audio"
    os.makedirs(folder,exist_ok=True)

    path=f"{folder}/{id}.mp3"

    if not os.path.exists(path):

        tts=gTTS(text)
        tts.save(path)

    return "/"+path