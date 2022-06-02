from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponseNotFound
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

def edit(request, id):
    try:
        user = User.objects.get(id=id)
        if request.method == "POST":
            user.name = request.POST.get("name")
            user.age = request.POST.get("age")
            user.birth = request.POST.get("birth")
            user.save()
            return HttpResponseRedirect('/')
        else:
            return render(request, 'forms_app/edit.html', {"user":user})
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")

def delete(request, id):
    try:
        user = User.objects.get(id=id)
        user.delete()
        return HttpResponseRedirect('/')
    except User.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")