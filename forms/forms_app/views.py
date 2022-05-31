from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import User
# Create your views here.
def index(request):
    user = User.objects.all()
    return render(request, 'forms_app/home.html', {"user": user})

def create(request):
    if request.method == 'POST':
        klient = User()
        klient.name = request.POST.get('name')
        klient.age = request.POST.get('age')
        klient.birth = request.POST.get('birth')
        klient.save()
    return HttpResponseRedirect('/')
