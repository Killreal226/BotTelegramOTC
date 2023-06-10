from pyrogram.errors import FloodWait
from pyrogram import Client
import time

from settings import *

def main():
    with Client("my_account", api_id, api_hash) as app:
        with open ('message.txt') as ms:
            app.send_message(adress, f"{ms.read()}")
        
    
def create_OTC_adress():
    OTC_list = open('OTC.txt', 'r', encoding='utf-8').readlines()
    OTC = []
    for adress in OTC_list:
        OTC.append('@' + adress.split('/')[-1].split()[0])
    return(OTC)

api_id = API_ID
api_hash = API_HASH 

kd_limit = input('введи кд: ')

OTC_adress = create_OTC_adress()

while True:
    for adress in OTC_adress:
        #chat_join()
        send_time = time.strftime('%H:%M:%S')
        try:
            main()
            print(f'{send_time} сообщение отправлено в {adress}')
        except FloodWait as e:
            print(f'{send_time} ошибка флуда, ждать осталось {e.value} секунд')
            time.sleep(e.value + 3)
        except:
            print(f'{send_time} не прошло кд в {adress}')
            continue
    time.sleep(int(kd_limit))
