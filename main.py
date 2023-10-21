import requests
from settings import TOKEN





def get_headers():
    return{
        'Content-Type': 'application/json',
        'Authorization': f'OAuth {TOKEN}'
    }


def create_folder(folder_name):
    uri = f'v1/disk/resources'
    base_host = 'https://cloud-api.yandex.net/'
    request_url = base_host + uri
    params = {'path': f'{folder_name}', 'fields': 1}
    response = requests.put(request_url, headers=get_headers(), params=params)
    return response



