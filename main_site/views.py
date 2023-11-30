from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.urls import reverse


from .models import user, product, watchlist

# Create your views here.

def index(request):
    if request.method == "GET":
        current_user = request.session.session_key 
        request.session['init'] = True  # This modifies the session
        request.session.save()
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
            "user": user.objects.all() , "current_user": current_user, "product": product.objects.all()  
        })
    else:
        if request.POST.get("product_id", None):
            item = product.objects.get(id=request.POST["product_id"])
            userr = user.objects.get(sess=request.session.session_key)
            if watchlist.objects.filter(client=userr, item=item):
                return HttpResponseRedirect(reverse("index")) 
            else: 
                item = product.objects.get(id=request.POST["product_id"])
                new_watchlist = watchlist(
                    client=userr,
                    item=item,
                )
                new_watchlist.save()
                return HttpResponseRedirect(reverse("index"))


def watch_list(request):
    current_user = user.objects.get(sess=request.session.session_key)
    if request.method == "POST":
        return render(request, "site_temp/index.html")
    else:
        return render(request, "site_temp/watchlist.html", {
            "item": current_user.user_watchlist.all(),
            "products": product
        })