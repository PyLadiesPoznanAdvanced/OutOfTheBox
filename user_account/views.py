from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout # authenticate user
from django.contrib.auth.decorators import login_required

# Create your views here.

def start_page(request):
    return render(request, 'user_account/base.html')


def login_view(request):
    ''' metoda logowania - po zalogowaniu, udanym lub nie udanym, przekierowywuje do strony glowne, czyli http://127.0.0.1:5000/
        jezeli logowanie bylo udane, pokazuje sie napis "Czy chcesz sie wylogować?
        miejsce przekierowanie ustalone jest w pliku settings.py na samym dole: LOGIN_REDIRECT
    '''
    username = request.POST.get('username')  # == request.POST['username']
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
    return redirect('user_account:start_page')

@login_required(login_url='/')
def logout_view(request):
    logout(request)
    return redirect('user_account:start_page')

def register(request):
    return render(request, 'user_account/base.html')