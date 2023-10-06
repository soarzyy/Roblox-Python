import requests
import random

#put ur cookie here
cookie=("")
#put ur group id here
groupid=("")

# vars
url = f'https://groups.roblox.com/v1/groups/{groupid}/status'
token = requests.post('https://auth.roblox.com/v1/login', cookies = {".ROBLOSECURITY":cookie})
xcrsf = (token.headers['x-csrf-token'])
header = {'X-CSRF-TOKEN': xcrsf}

# random quote from the quran
def get_random_verse():
    verses = requests.get(f"https://api.alquran.cloud/v1/surah/{random.randint(1, 114)}/en.sahih").json()['data']['ayahs']
    return verses[random.randint(1, len(verses))]['text']

#script
groupshout= f'"{get_random_verse()}"'
shout={"message": f"{groupshout}"}
g = requests.patch(url, data = shout, headers = header, cookies = {".ROBLOSECURITY":cookie})

print(g.json())
