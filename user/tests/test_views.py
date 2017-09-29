from django.test import TestCase, Client
from django.urls import reverse
from user.models import User

class UserTestCase(TestCase):
    """
    tast case for user model
    """

    def setUp(self):
        client = Client()
        model = User()
        model.username = 'admin2'
        model.password = model.hash_password('admin2')
        model.save()


    def test_login_not_validate(self):
        """
            test for user login with empty password value or username
        """
        response = self.client.post(reverse('login'), {'username':'admin2',})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'login failed.'}
        )
    

    def test_login_logged_in(self):
        """
            test for user login with correct data
        """
        response = self.client.post(reverse('login'), {'username':'admin2', 'password': 'admin2'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'Logged in.'}
        )


    def test_registration_not_validate(self):
        """
            test for user registratio with badd password or username
        """
        response = self.client.post(reverse('registration'), {'username':'admin2',})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'Validation failed.'}
        )


    def test_registration_success(self):
        """
            test for user registration with correct data
        """
        response = self.client.post(reverse('registration'), {'username':'admintest', 'password': 'admintest'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'User created.'}
        )


    def test_registration_user_exists(self):
        """
            test for user registration with existing user
        """
        response = self.client.post(reverse('registration'), {'username':'admin2', 'password': 'admin2'})
        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'User already exists.'}
        )

