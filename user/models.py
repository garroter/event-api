from django.db import models
import hashlib
from django.conf import settings

class User(models.Model):
    """
        user model
    """
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)


    def hash_password(self, password):
        """
             fucntion for hash user password with salt fron config file
        """
        hash_password = password + settings.PASSWORD_SALT
        return hashlib.md5(hash_password.encode('utf-8')).hexdigest()


    def if_exists(self, username):
        """
        function checking if user exists in database
        """
        try:
            return User.objects.filter(username = username).get()
        except User.DoesNotExist:    
            return False


    def is_valid(self, request, scenario):
        """
            function for validate data from post request
        """
        if request.method == 'POST' and 'username' in request.POST and 'password' in request.POST:
            
            user_exists = self.if_exists(request.POST['username'])
            if user_exists:
                if scenario == 'registration':
                    return 'exists'
                else:
                    return user_exists
            elif scenario == 'registration': 
                self.username = request.POST['username']
                self.password = self.hash_password(request.POST['password'])
                self.save()
                return 'created'
        else:
            return 'not validate'
                

    def login(self, request):        
        """ 
        function for validate username and password
        """
        user = self.is_valid(request, 'login')

        if user == 'not validate':
            return False
        else:
            try:
                if request.POST['username'] == user.username and self.hash_password(request.POST['password']) == user.password:
                    return True
                else:
                    return False
            except User.DoesNotExist:    
                return False       


    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username