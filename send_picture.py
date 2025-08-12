import os
import requests
import dotenv


dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
pic_path = r'files\files\IXKP8281.JPG'
chat_ids = [6736740776,5412578346]  

def sendPhoto(chat_ids , pic_path):
    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{TOKEN}/sendPhoto"  
        with open(pic_path, 'rb') as photo:
            files = {"photo": photo}
            data = {"chat_id": chat_id}
            response = requests.post(url, data=data, files=files)
            print(response.json()) 

            
sendPhoto(chat_ids , pic_path)            
