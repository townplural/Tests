import unittest
from unittest import TestCase
import requests
from main import get_headers, create_folder

class TestFolderCreation(TestCase):
    def test_create_folder(self):
        request_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        folder_name = '123321'
        params = {'path': f'{folder_name}', 'fields': 1}
        expected = requests.put(request_url, headers=get_headers(), params=params)
        result = create_folder('123321')
        self.assertEqual(expected, result)

    @unittest.skipIf()
    def test_same_name_folder(self):


