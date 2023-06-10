import asyncio
from pyrogram.errors import FloodWait
from pyrogram import Client
import time

from settings import * 

        
def chat_join():
    with Client("my_account", api_id, api_hash) as app:
        app.join_chat(adress)
    
def create_OTC_adress():
    OTC_list = open('OTC.txt', 'r', encoding='utf-8').readlines()
    OTC = []
    for adress in OTC_list:
        OTC.append('@' + adress.split('/')[-1].split()[0])
    return(OTC)

api_id = API_ID
api_hash = API_HASH

OTC_adress = create_OTC_adress()

for adress in OTC_adress:
        send_time = time.strftime('%H:%M:%S')
        try:
            chat_join()
            print(f'{send_time} присоеденился к {adress}')
        except FloodWait as e:
            print(f'{send_time} ошибка флуда, ждать осталось {e.value} секунд')
            time.sleep(e.value + 3)
            chat_join()
            print(f'{send_time} присоеденился к {adress}')
        except:
            print(f'{send_time} не удалось присоедениться к {adress}')
            continue
        time.sleep(120)
print('конец')
            
        

