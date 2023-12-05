from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login, logout
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User 


# Create your views here.

# login
@csrf_exempt
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            return HttpResponse('Erro ao logar')
    template = loader.get_template('login.html')
    return HttpResponse(template.render({}, request))

# cadastro
@csrf_exempt
def cadastro(request):
    if request.method == 'POST':
        template = loader.get_template('cadastro.html')
        nome = request.POST.get('nomeusuario')
        usernamee = request.POST.get('loginusuario')
        passwordd = request.POST.get('senhausuario')
        user = User.objects.create_user(username=usernamee, password=passwordd,)
        user.save()
        user = authenticate(request, username=usernamee, password=passwordd)
        if user is not None:
            login(request, user)
            template = loader.get_template('login.html')
    template = loader.get_template('cadastro.html')
    return HttpResponse(template.render({}, request))

# logOut
def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


