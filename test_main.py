import unittest
from unittest import TestCase
import requests
from main import get_headers, create_folder


class TestFolderCreation(TestCase):

    def test_create_folder(self):
        request_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        folder_name = '123321'
        params = {'path': f'{folder_name}', 'fields': 1}
        result = requests.put(request_url, headers=get_headers(), params=params)
        expected = '{"href":"https://cloud-api.yandex.net/v1/disk/resources?path=disk%3A%2F123321","method":"GET",' \
                   '"templated":false}'
        self.assertEqual(expected, result.text)

    @unittest.expectedFailure
    def test_same_name_folder(self):
        expected2 = '<Response [200]>'
        response = create_folder('123321')
        self.assertEqual(expected2, f'{response}')

