from dotenv import load_dotenv
import os
import random
import urllib.parse

import requests


def download_comic(comic_number):
    url = f'https://xkcd.com/{comic_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    json_response = response.json()
    parsed_url = urllib.parse.urlsplit(
        json_response['img'],
        scheme='',
        allow_fragments=True
    )
    scheme, netloc, path, *others =  parsed_url
    file_name = os.path.basename(path)
    comment = json_response['alt']
    response_pic = requests.get(json_response['img'])
    response_pic.raise_for_status()
    with open(file_name, 'wb') as file:
        file.write(response_pic.content)
    return file_name, comment


def get_wall_upload_server(vk_token, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    payload = {
        'group_id': group_id,
        'access_token': vk_token,
        'v': '5.131'
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()['response']['upload_url']


def upload_image(upload_url, file_name):
    with open(file_name, 'rb') as file:
        files = {
            'photo': file
        }
        response = requests.post(upload_url, files=files)
    response.raise_for_status()
    json_response = response.json()
    return json_response['server'], json_response['photo'], json_response['hash']


def save_wall_image(vk_token, server, photo, file_hash, group_id):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    payload = {
        'group_id': group_id,
        'access_token': vk_token,
        'server': server,
        'photo': photo,
        'hash': file_hash,
        'v': '5.131'
    }
    response = requests.post(url, params=payload)
    response.raise_for_status()
    json_response = response.json()['response'][0]
    return json_response['owner_id'], json_response['id']


def post_image(vk_token, owner_id, media_id, comment, group_id):
    url = 'https://api.vk.com/method/wall.post'
    payload = {
        'owner_id': f'-{group_id}',
        'from_group': 1,
        'access_token': vk_token,
        'attachments': f'photo{owner_id}_{media_id}',
        'message': comment,
        'v': '5.131'
    }
    response = requests.post(url, params=payload)
    response.raise_for_status()


def get_comic_number():
    url = 'https://xkcd.com/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    comic_number = response.json()['num']
    return comic_number


def main():
    load_dotenv()
    vk_token = os.environ['ACCESS_TOKEN']
    group_id = os.environ['GROUP_ID']
    try:
        comic_number = random.randint(1, get_comic_number())
        file_name, comment = download_comic(comic_number)
        upload_url = get_wall_upload_server(vk_token, group_id)
        server, photo, file_hash = upload_image(upload_url, file_name)
        owner_id, media_id = save_wall_image(
            vk_token,
            server,
            photo,
            file_hash,
            group_id
        )
        post_image(vk_token, owner_id, media_id, comment, group_id)
    finally:
        os.remove(file_name)


if __name__ == '__main__':
    main()
