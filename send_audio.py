import os
import requests
import dotenv


dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
audio_path = r'files\files\audio.mp3'
chat_ids = [6736740776,5412578346]  

def sendAudio(chat_ids , audio_path):
    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{TOKEN}/sendAudio"  
        with open(audio_path, 'rb') as audio:
            files = {"audio": audio}
            data = {"chat_id": chat_id}
            response = requests.post(url, data=data, files=files)
            print(response.json()) 

            
sendAudio(chat_ids , audio_path)  