from django.test import TestCase
from event.models import Event

class EventTestCase(TestCase):
    """
    tast case for event model
    """

    def setUp(self):
        model = Event(name='test', lat='123.456', lon='6745.78454')
        model.save()


    def test_model_get(self):
        event = Event.objects.get(name='test')
        self.assertEqual(event.name, 'test')


