import requests
import time
import random
#sry for the messy code

# put your roblox cookie
cookie=('')
# put ur roblox pin
urpin=('')


# vars
url = 'https://auth.roblox.com/v1/account/pin/unlock'
url2 = 'https://auth.roblox.com/v1/account/pin/lock'
url3 = 'https://users.roblox.com/v1/description'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

#gets ur username
username = requests.get("https://users.roblox.com/v1/users/authenticated",cookies={".ROBLOSECURITY":cookie}).json()['name']

pin = {'pin': f'{urpin}'}

#get random quote from the quran
def get_random_verse():
    verses = requests.get(f"https://api.alquran.cloud/v1/surah/{random.randint(1, 114)}/en.sahih").json()['data']['ayahs']
    return verses[random.randint(1, len(verses))]['text']

quote = f'"{get_random_verse()}"'

#set the discription
description = {"description": f"{quote}"}

#unlocks ur pin then sets the discription and locks the pin again
r = requests.post(url, data = pin, headers = header, cookies = {".ROBLOSECURITY":cookie})
time.sleep(1)
d = requests.post(url3, data = description, headers=header, cookies = {".ROBLOSECURITY":cookie})

print(username)
print(r.json())
print(d.json())

time.sleep(5)
l = requests.post(url2, headers = header, cookies = {".ROBLOSECURITY":cookie})

print(l.json())

