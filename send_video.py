import os
import requests
import dotenv



dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
vid_path = r'files/file/Banda Ban Ja - Garry Sandhu.mp4'
chat_id = 5211817036

def sendVideo(chat_id, vid_path):
    with open(vid_path, 'rb') as video:
        files = {"video": video}
        data = {"chat_id": chat_id}
        response = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendVideo",data = data,files = files )
        print(response.json())

sendVideo(chat_id, vid_path)         

            
