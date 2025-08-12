import os
import requests
import threading
import dotenv


dotenv.load_dotenv()                     ## load token number
TOKEN = os.getenv("BOT_TOKEN")


file_path =  r'files\files\unit1_half.pdf'           ## file path name
chat_ids = [6736740776,5412578346]                    ## chat id of people who started my bot

def send_documents(chat_ids , file_path):
    url = f"https://api.telegram.org/bot{TOKEN}/sendDocument"      
    # Print the response from the API
    for chat_id in chat_ids:
        with open(file_path, 'rb') as f:          ## open file represented as f
            files = {"document": f}               ## data includes chat id
            data = {"chat_id": chat_id }
            response = requests.post(url, data=data, files=files)     ## if we want to send document,picture we use post request
            print(response.json())


send_documents(chat_ids , file_path)
