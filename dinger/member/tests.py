import datetime
from django.test import TestCase
from models import User, Photo

from views import new_user, login_user
# Create your tests here.

class MemberTestCase(TestCase):
    def setUp(self):
        Photo.objects.create()
        Photo.objects.create()
        Photo.objects.create()

        users = [
            {
                'username': 'google',
                'password': '123456',
                'email': 'mail@gmail.com',
                'name': 'GW Koh',
                'birthday': datetime.date(1992,1,1),
                'intro': 'hello',
                'phone': '01051483415'
            },
            {
                'username': 'silvara',
                'password': '123qwe',
                'email': 'jaminip@gmail.com',
                'name': 'jm Cho',
                'birthday': datetime.date(1992,2,2),
                'intro': 'hello nice to meet you',
                'phone': '01000000000'
            },
            {
                'username': 'random',
                'password': 'j134890',
                'email': 'ad@unist.ac.kr',
                'name': 'NONO',
                'birthday': datetime.date(1994,12,25),
                'intro': 'hello..',
                'phone': '01099999999'
            }]

        for user in users:
            new_user(user)


    def test_members(self):
        tries = [('google', '123456', True),
                ('silvara', '123456', False),
                ('silvara', '123qwe', True),
                ('random', 'j134890', True),
                ('geegoe', '123123', False)]

        for un, pw, b in tries:
            if b:
                self.assertNotEqual(login_user(un, pw), None)
            else:
                self.assertEqual(login_user(un, pw), None)


