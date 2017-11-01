from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def logout_view(request):
    """завершает сеанс работы с приложением"""
    logout(request)
    return HttpResponseRedirect(reverse('a_blog:index'))

def register(request):
    """регистрирует нового пользователя"""
    if request.method != 'POST':
        #display blank registration form
        form = UserCreationForm()

    else:
        #обработка заполненной формы
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            #выполнение входа и перенаправление на домашнюю страницу

            authenticated_user = authenticate(username=new_user.username, 
                    password=request.POST['password1'])

            login(request, authenticated_user)

            return HttpResponseRedirect(reverse('a_blog:blogs'))

    context = {'form': form}
    return render(request, 'users/register.html', context)
