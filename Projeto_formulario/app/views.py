from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Formulário de Cadastro
def create(request):
    return render(request, 'create.html')

# Inserção dos Dados
def store(request):
    
    data = {}

    if(request.POST['password'] != request.POST['password-conf']):
        data['msg'] = 'Senhas diferentes!'
        data['class'] = 'alert-danger'
        return render(request, 'create.html', data)
    else:
        user = User.objects.create_user(request.POST['email'], request.POST['username'], request.POST['password'])
        user.first_name = request.POST['name']
        data['class'] = 'alert-success'
        data['msg'] = 'Usuário Cadastrado!'
        user.save()   
        return render(request, 'create.html', data)
 

# Formulário de Login e página inicial
def onlogin(request):
    return render(request, 'login.html')

# Processar o Login
def dologin(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        return redirect('/dashboard/')

def dashboard(request):
    return render(request, 'dashboard/home.html')