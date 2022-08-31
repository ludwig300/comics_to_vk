import requests
import random
import os
from downloader import download_image
from extension import get_extension
from dotenv import load_dotenv


def get_comics(comics_number):
    url = f'https://xkcd.com/{comics_number}/info.0.json'
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


def get_group_id(token_vk):
    url = 'https://api.vk.com/method/groups.get'
    payload = {
        'extended': 0,
        'access_token': token_vk,
        'v': '5.131'
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    group_id = response.json()['response']['items']
    return group_id


def get_wall_upload_server(token_vk, group_id):
    url = 'https://api.vk.com/method/photos.getWallUploadServer'
    payload = {
        'group_id': group_id,
        'access_token': token_vk,
        'v': '5.131'
    }
    response = requests.get(url, params=payload)
    response.raise_for_status()
    return response.json()


def upload_image(upload_url, comics_file):
    with open(comics_file, 'rb') as file:
        files = {
            'photo': file
        }
        response = requests.post(upload_url, files=files)
        response.raise_for_status()
        return response.json()


def save_wall_photo(token_vk, server, photo, hash, group_id):
    url = 'https://api.vk.com/method/photos.saveWallPhoto'
    payload = {
        'group_id': group_id,
        'access_token': token_vk,
        'server': server,
        'photo': photo,
        'hash': hash,
        'v': '5.131'
    }
    response = requests.post(url, params=payload)
    response.raise_for_status()
    return response.json()


def posting_image(token_vk, owner_id, media_id, comments, group_id):
    url = 'https://api.vk.com/method/wall.post'
    payload = {
        'owner_id': f'-{group_id}',
        'from_group': 1,
        'access_token': token_vk,
        'attachments': f'photo{owner_id}_{media_id}',
        'message': comments,
        'v': '5.131'
    }
    response = requests.post(url, params=payload)
    response.raise_for_status()


def main():
    load_dotenv()
    token_vk = os.environ['ACCESS_TOKEN']
    group_id = get_group_id(token_vk)[0]
    comics_number = random.randint(1, 2665)
    comics = get_comics(comics_number)
    extension_img = get_extension(comics['img'])
    comments = comics['alt']
    comics_file = f'comics_{comics_number}{extension_img}'
    path = os.path.join('.', comics_file)
    download_image(comics['img'], path)
    upload_server = get_wall_upload_server(token_vk, group_id)
    upload_url = upload_server['response']['upload_url']
    response_upload_image = upload_image(upload_url, comics_file)
    server = response_upload_image['server']
    photo = response_upload_image['photo']
    hash = response_upload_image['hash']
    response_wall_photo = save_wall_photo(
        token_vk,
        server,
        photo,
        hash,
        group_id
    )
    owner_id = response_wall_photo['response'][0]['owner_id']
    media_id = response_wall_photo['response'][0]['id']
    posting_image(token_vk, owner_id, media_id, comments, group_id)
    os.remove(comics_file)


if __name__ == '__main__':
    main()
