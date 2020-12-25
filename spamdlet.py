import requests as rq
import threading
import os
import time


os.system("clear")
print(f"""
   _____                           ____     __
  / ___/____  ____ _____ ___  ____/ / /__  / /_
  \__ \/ __ \/ __ `/ __ `__ \/ __  / / _ \/ __/
 ___/ / /_/ / /_/ / / / / / / /_/ / /  __/ /_
/____/ .___/\__,_/_/ /_/ /_/\__,_/_/\___/\__/
    /_/
               𝘣𝘺 𝘒𝘰𝘥𝘻𝘪𝘮𝘢
""")
time.sleep(2)
print('\n\n\n\n')

threads = 1

wall_id = int(input('Введите wall_id: '))
wall_section_id = int(input('Введите wall_section_id: '))
attachment = input('Введите ссылку на вложение, которым хотите спамить (будь-то фото или ссылка на ютуб): ')
subject = input('Введите заголовок для вложения (по желанию): ')
body = input('Введите текст для вложения (по желанию): ')
threads = int(input('Введите количество потоков для спамма (по умолчанию 1): '))

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    'authorization' : 'Bearer 63002bc7cc05f2a3157ad7945e958e22cde27e81358c16ec53c7082b151a8010'
}

payload = {
    'wall_id' : wall_id,
    'wall_section_id' : wall_section_id,
    'attachment' : attachment,
    'body' : body,
    'subject' : subject,
    'cid' :	'c_new5'
}


def main():
    while True:
        response = rq.post('https://padlet.com/api/3/wishes', headers = headers, data = payload)
        if response.status_code == 201:
            print('Отправлено успешно')
        else:
            print('Что-то пошло не так...')

for i in range(threads):
    x = threading.Thread(target = main)
    x.start()
