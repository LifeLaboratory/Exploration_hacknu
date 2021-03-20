from unittest import TestCase
from app.users.processor import Processor
from pprint import pprint


class TestAitu(TestCase):

    def test_dev(self):
        Processor().login({
            'id': '1',
            'avatar': 'https://avatars.githubusercontent.com/u/23695322?s=400&v=4',
            'description': 'asdaasdsd',
            'name': 'name',
            'lastname': 'lastname',
            'avatarThumb': 'avatarThumb',
            'phone': 'phone',
            'latitude': 123.123,
            'longitude': 123.123,
        })

    def test_dev_2(self):
        pprint(Processor().get_next_user({
            'id': '1'
        }))

    def test_dev_3(self):
        pprint(Processor().get_meeting({
            'id': '4',
        }))
