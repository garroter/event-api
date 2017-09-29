from django.http import JsonResponse
from django.conf import settings
from user.models import User


def registration(request):
    """
        registration view and validation
    """
    user = User()
    validate = user.is_valid(request, 'registration')
    print(request.session.get('user'))
    if validate == 'exists':
        response = {'status': 'User already exists.'}
    elif validate == 'created':
        response = {'status': 'User created.'}
    else:
        response = {'status': 'Validation failed.'}
    
    return JsonResponse(response)


def login(request):
    """
    login view with session
    """
    user = User()
    if user.login(request):
        request.session['user'] =  True
        response = {'status': 'Logged in.'}
    else:
        response = {'status': 'login failed.'}
            
    return JsonResponse(response)


def logout(request):
    """ 
        function to logged out a user,
    """     
    if request.session.get('user'):
        del request.session['user']
        response = {'status': 'loged out.'}
    else:
        response = {'status': 'you are logged out.'}    
    
    return JsonResponse(response)    