from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect

from .FormRegisterProduct import FormRegisterProduct
from .FormLoginUser import FormLoginUser
from .RegisterUser import RegisterUser
from .RegisterClient import RegisterClient
from .RegisterCustommer import RegisterCustommer

from django.contrib import messages
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.models import User

def index(request):
    return render(request, 'Index.html', {
        #context
    })
def loginUser(request):
    formLogin = FormLoginUser()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvendio {}'.format(user.username))
            return redirect('registerProducts')
        else:
            messages.error(request, 'Usario o Contraseña son invalidos')

    return render(request, 'Users/Login.html', {
        'form': formLogin

    })
def logoutUser(request):
    logout(request)
    messages.success(request, 'Session Cerrada')
    return redirect('loginUser')
def registerUser(request):
    formRegister = RegisterUser(request.POST or None)
    if request.method == 'POST' and formRegister.is_valid():
        username = formRegister.cleaned_data.get('username')
        email = formRegister.cleaned_data.get('email')
        password = formRegister.cleaned_data.get('password')
        user = User.objects.create_user(username, email, password)
        if user:
            messages.success(request, 'Usuario Creado')
            return redirect('registerProducts')
        else:
            messages.error(request, '<Usuario No Creado')
    return render(request, 'Users/registerUser.html',{
        'form': formRegister
    })
def registerClient(request):
    formClient = RegisterClient()
    return render(request, 'RegisterClient.html', {
        'form': formClient
    })
def registerCustommer(request):
    formCustommer = RegisterCustommer()
    return render(request, 'RegisterCustommer.html', {
        'form': formCustommer
    })
def registerProducts(request):
    formProduct = FormRegisterProduct()
    return render(request, 'RegisterProduct.html', {
        'form': formProduct
    })
