import requests
import json

url = 'https://gist.githubusercontent.com/KotovVitaliy/83e4eeabdd556431374dfc70d0ba9d37/raw'

response = requests.get(url)
text = response.text.strip().strip('"')   # убираем кавычки по краям

obj = json.loads(text)
print(obj['messages'][1]['message'])