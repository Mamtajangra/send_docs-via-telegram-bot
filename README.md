
# Send Documents, Audio, Video, and Pictures via Telegram Bot

This project provides Python scripts to send documents, audio files, videos, and pictures to Telegram users using the Telegram Bot API.
![Bot Screenshot](files\files\result.jpg)

## Features

- **Send Documents:** Easily send PDF or other document files.
- **Send Audio:** Share audio files (e.g., MP3) with users.
- **Send Video:** Send video files to Telegram chats.
- **Send Pictures:** Share images with your contacts.
- **Multiple Recipients:** Send files to multiple chat IDs at once.
- **Environment Variables:** Securely manage your bot token using a `.env` file.

## Requirements

- Python 3.x
- Install dependencies:
  ```sh
  pip install requests python-dotenv

## Setup

1. Clone the repository and navigate to the project folder.
2. Create a .env file in the project root with your Telegram bot token:

    BOT_TOKEN=your_telegram_bot_token

3. Place your files in the files/files/ directory:

- Documents (e.g., unit1_half.pdf)
- Audio (e.g., audio.mp3)
- Video (e.g., Banda Ban Ja - Garry Sandhu.mp4)
- Pictures (e.g., IXKP8281.JPG)

## Usage
Run the corresponding script to send a file type:

- Send Document:
python [send_docs.py](http://_vscodecontentref_/0)

- Send Audio:
python [send_audio.py](http://_vscodecontentref_/1)

- Send Video:
python [send_video.py](http://_vscodecontentref_/2)

- Send Picture: 
python [send_picture.py](http://_vscodecontentref_/3)

## Each script:

- Loads your bot token from .env
- Reads the file from the files/files/ directory
- Sends the file to all chat IDs listed in the script

## File Structure

[send_audio.py](http://_vscodecontentref_/4)
[send_docs.py](http://_vscodecontentref_/5)
[send_picture.py](http://_vscodecontentref_/6)
[send_video.py](http://_vscodecontentref_/7)
.env
[README.md](http://_vscodecontentref_/8)
files/
  files/
    audio.mp3
    unit1_half.pdf
    Banda Ban Ja - Garry Sandhu.mp4
    IXKP8281.JPG

## Notes
- Update the chat_ids list in each script with your target Telegram chat IDs.
- The scripts print the Telegram API response for each send attempt.  



..This project demonstrates how to automate sending various file types via Telegram using Python.