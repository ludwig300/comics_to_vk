import requests
import os
from dotenv import load_dotenv


def get_token_vk(client_id):
    url_oath = 'https://oauth.vk.com/authorize'
    payload = {
        'client_id': client_id,
        'display': 'page',
        'scope': 'photos,groups,wall,offline',
        'response_type': 'token'
    }
    response = requests.get(url_oath, params=payload)
    return response.url


def main():
    load_dotenv()
    client_id = os.environ['CLIENT_ID']
    print(get_token_vk(client_id))


if __name__ == '__main__':
    main()