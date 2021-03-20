from unittest import TestCase
from app.users.processor import Processor


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
        Processor().swipe({
            'id_first': '1',
            'id_second': '3',
            'status': True,
        })

    def test_dev_3(self):
        from pprint import pprint
        pprint(Processor().get_meeting({
            'id': '4',
        }))
