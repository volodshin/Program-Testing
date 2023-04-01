from loguru import logger
import requests
import time
import json
from config import API_KEY

def get_resp():
    response = requests.get(f"{API_KEY}")

    data = response.json()
    gender = data['gender']
    name = data['name']
    print(f'Gender: {gender}\nName: {name}')

    start_time = time.time()
    func_time = time.time() - start_time

    logger.info(f'\nPredict the gender of a person based on their name.\nStatus: {response}\nExecution time:{func_time} seconds')

get_resp()