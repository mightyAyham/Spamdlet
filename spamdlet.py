import requests as rq
import threading
import os
import time
import json


os.system("clear")
print(f"""
   _____                           ____     __
  / ___/____  ____ _____ ___  ____/ / /__  / /_
  \__ \/ __ \/ __ `/ __ `__ \/ __  / / _ \/ __/
 ___/ / /_/ / /_/ / / / / / / /_/ / /  __/ /_
/____/ .___/\__,_/_/ /_/ /_/\__,_/_/\___/\__/
    /_/
              
(the script uses random photos of your choice using unsplash.com)
               
""")
time.sleep(2)

threads = 1

search = input("search for an image: ").replace(" ", "+")

wall_id = int(input('input the wall_id: '))
subject = input('choose a subject (optional): ')
body = input('choose text (optional): ')
threads = int(input('number of CPU threads to use (default is 1): '))

headers = {
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0',
    'authorization' : 'Bearer 63002bc7cc05f2a3157ad7945e958e22cde27e81358c16ec53c7082b151a8010'
}


def main():
    i = 1
    while True:
        response = rq.get(f"https://unsplash.com/napi/search/photos?query={search}&per_page=20&page={i}").text
        img = json.loads(response)
        for results in img['results']:
            payload = {
                            'wall_id' : wall_id,
                            'attachment' : results['urls']['full'],
                            'body' : body,
                            'subject' : subject,
                            'cid' :	'c_new5'
                        }
            response = rq.post('https://padlet.com/api/3/wishes', headers = headers, data = payload)
            if response.status_code == 201:
                print('sumbitted successfully')
            else:
                print(response.status_code)
                print('Something went wrong...')


            
        i += 1

for i in range(threads):
    x = threading.Thread(target = main)
    x.start()
