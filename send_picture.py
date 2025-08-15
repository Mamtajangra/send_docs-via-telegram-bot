import os
import requests
import threading
import dotenv


dotenv.load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")
pic_path = r'files\files\IXKP8281.JPG'
chat_ids = [6736740776,4947220003]

def sendPhoto(chat_ids , pic_path):
    with open(pic_path, 'rb') as photo:
        files = {"photo": photo}
        data = {"chat_id": chat_id}
        response = requests.post(f"https://api.telegram.org/bot{TOKEN}/sendPhoto",data = data,files = files )
        print(response.json()) 

            
  
list_of_threads = []

for chat_id in chat_ids:
    for i in range(2):
        g = threading.Thread(target=sendPhoto, args=(chat_id, pic_path))
        list_of_threads.append(g)
        g.start()


for thread in list_of_threads:
    thread.join()         
