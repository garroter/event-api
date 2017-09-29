from django.test import TestCase, Client
from django.urls import reverse
from event.models import Event

class EventTestCase(TestCase):
    """
    tast case for event views
    """

    def setUp(self):
        client = Client()
        model = Event()
        model.name = 'test'
        model.lat = '123.456'
        model.lon = '543.67676'
        model.save()


    def test_event_list_no_logged_in(self):
        """
            test event list for not logged users, we expect json status: You are not logged in.
        """
        session = self.client.session
        session['user'] = False
        session.save()

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session["user"], False)
        self.assertJSONEqual(
            str(response.content, encoding='utf8'),
            {'status': 'You are not logged in.'}
        )
    
    
    def test_event_list_logged_in(self):
        """
            test event list for logged users, we expect json status: Event list.
        """
        session = self.client.session
        session['user'] = True
        session.save()

        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(self.client.session["user"], True)
        self.assertContains(response, "Event list")


