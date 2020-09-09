from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Prispevok
# Create your views here.
def ForumView(request):
    return HttpResponse('<p>'.join([prispevok.obsah for prispevok in Prispevok.objects.all()]))
