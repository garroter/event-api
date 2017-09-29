from django.http import JsonResponse
from django.core import serializers
from event.models import Event


def index(request):
    """
        event list with all recors, visible only for logged users
    """

    if request.session.get('user'):
       events = serializers.serialize('json', Event.objects.all()) 
       response = {'status': 'Event list', 'data': events}
    else:
        response = {'status': 'You are not logged in.'}

    return JsonResponse(response)
