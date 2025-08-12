import os
import requests
import dotenv


dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
video_path = r'files\files\Banda Ban Ja - Garry Sandhu.mp4'
chat_ids = [6736740776,5412578346]  

def sendVideo(chat_ids , video_path):
    for chat_id in chat_ids:
        url = f"https://api.telegram.org/bot{TOKEN}/sendVideo"  
        with open(video_path, 'rb') as video:
            files = {"video": video}
            data = {"chat_id": chat_id}
            response = requests.post(url, data=data, files=files)
            print(response.json()) 

            
sendVideo(chat_ids , video_path)            
