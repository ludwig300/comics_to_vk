import argparse

import requests


def get_group_id(access_token):
    url = 'https://api.vk.com/method/groups.get'
    payload = {
        'extended': 0,
        'access_token': access_token,
        'v': '5.131'
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['response']['items'][0]


def createParser():
    parser = argparse.ArgumentParser(description='Get "group_id"')
    parser.add_argument('access_token', help='`access_token` can be obtained using `get_token_vk.py`')
    return parser


def main():
    parser = createParser()
    namespace = parser.parse_args()
    print('group_id:', get_group_id(namespace.access_token))


if __name__ == '__main__':
    main()
