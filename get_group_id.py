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


def create_parser():
    parser = argparse.ArgumentParser(description='Get "group_id"')
    parser.add_argument('access_token', help='`access_token` can be obtained using `get_token_vk.py`')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print('group_id:', get_group_id(args.access_token))


if __name__ == '__main__':
    main()
