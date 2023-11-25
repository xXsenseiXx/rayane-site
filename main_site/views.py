from django.http import HttpResponse
from django.shortcuts import render
from .models import user
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def index(request):
    request.session['init'] = True  # This modifies the session
    current_user = request.session.session_key  # This gets the session key
    if current_user is not None:  # This checks if the session key is not None
        try:
            user.objects.get(sess=current_user)  # This checks if a user with the current session key already exists
        except ObjectDoesNotExist:  # This runs if a user with the current session key does not exist
            new_user = user (
                sess=current_user
            )
            new_user.save()
    return render(request, "site_temp/index.html", {
        "user": user , "current_user": current_user  
    })