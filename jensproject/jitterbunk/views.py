from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from datetime import datetime

from .models import Bunk, User, Bunkform
from .forms import BunkForm

def index(request):
    template = loader.get_template('jitterbunk/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

def bunks(request):
    bunks_list = Bunk.objects.order_by('-time')
    template = loader.get_template('jitterbunk/bunks.html')
    context = {
        'bunks_list': bunks_list,
    }
    #output = ', '.join([str(b) for b in bunks_list])
    #return HttpResponse(output)
    return HttpResponse(template.render(context, request))

def users(request):
    user_list = User.objects.order_by('username')
    template = loader.get_template('jitterbunk/users.html')
    context = {
        'user_list': user_list,
    }
    #return HttpResponse("This is user %s." % user_id)
    return HttpResponse(template.render(context, request))

def user(request, user_id):
    curr_user = User.objects.get(pk=user_id)
    bunks_from_list = Bunk.objects.filter(from_user_id=user_id) 
    bunks_to_list = Bunk.objects.filter(to_user_id=user_id)
    #bunks_list = Bunk.objects.all()
    template = loader.get_template('jitterbunk/user.html')
    context = {
        'user_id': user_id,
        'user': curr_user,
        'bunk_from_list': bunks_from_list,
        'bunk_to_list': bunks_to_list,
    }
    return HttpResponse(template.render(context, request))

def bunkform(request):
    template = loader.get_template('jitterbunk/bunkform.html')
    context = {}
    return HttpResponse(template.render(context, request))


def bunk_form(request):
    # if this is a POST request we need to process the form data
    if request.method == "POST":
        # create a form instance and populate it with data from the request:
        form = BunkForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            f_user = User.objects.get(username=request.POST.get('bunker'))
            t_user = User.objects.get(username=request.POST.get('bunked'))
            print(f_user)
            print(t_user)
            new_form = Bunkform(bunker=f_user, bunked=t_user)
            new_form.save()
            new_bunk = Bunk(from_user=f_user, to_user=t_user, time=datetime.now())
            new_bunk.save()
            #print()
            #print(u2)
            return render(request, 'jitterbunk/index.html')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = BunkForm()

    return render(request, "jitterbunk/bunkform.html", {"form": form})
