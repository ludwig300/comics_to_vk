import argparse

import requests


def get_token_vk(client_id):
    url_oath = 'https://oauth.vk.com/authorize'
    payload = {
        'client_id': client_id,
        'display': 'page',
        'scope': 'photos,groups,wall,offline',
        'response_type': 'token'
    }
    response = requests.get(url_oath, params=payload)
    response.raise_for_status()
    return response.url


def create_parser():
    parser = argparse.ArgumentParser(description='Get url for "access_token"')
    parser.add_argument('client_id', help='client_id can get after create app from https://vk.com/editapp?act=create')
    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()
    print(get_token_vk(args.client_id))


if __name__ == '__main__':
    main()
