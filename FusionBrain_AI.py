import requests
import json
import asyncio
import config

HEADERS = {
    'X-key' : f'Key {config.API_KEY}',
    'X-Secret' : f'Secret {config.SECRET_KEY}',

}
URL = 'https://api-key.fusionbrain.ai/'

acsyn def generate(prompt):
    params = {
        "type": "GENERATE",
        "numImages": 1,
        "style": "string",
        "width": 1024,
        "height": 1024,
        "generateParams": {"query" : prompt}
    }

    print(params)
    files = {
        'model_id' : (None, 4),
        'params' : (None, json.dumps(params), 'application/json')

    }

    response = requests.post(URL + "key/api/v1/text2image/run", headers = HEADERS, files = files)
    data = response.json()
    attempts = 0
    print(data)
    while attempts < 40:
        response = requests.get(URL + "key/api/v1/text2image/status/" + data['uuid'], headers = HEADERS)
        data = response.json()
        if data['status'] == 'DONE':
            return data['images']
        attempts += 1
        await asyncio.sleep(3)
