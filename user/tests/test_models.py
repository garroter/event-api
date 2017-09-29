from django.test import TestCase
from user.models import User
from django.conf import settings

class UserTestCase(TestCase):
    """
    tast case for user model
    """

    def setUp(self):
        model = User(username='test', password='password')
        model.save()


    def test_model_get(self):
        user = User.objects.get(username='test')
        self.assertEqual(user.username, 'test')


