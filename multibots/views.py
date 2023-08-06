from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.db.models import Q, F
import operator
from functools import reduce

from .forms import LoginForm
# from multibots.models import Mylink
import sys
import inspect

def home_view(request):

    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return render(request, 'home.html')

def login_view(request):
    form = LoginForm(request.POST or None)
    context = {
        'form': form
    }
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)

        try:
            lgn = login(request, user)
            return redirect(reverse('home_view'))
            # return render(request, "home.html")
        except Exception as e:
            print("\nmultibots.views.login_view Exception= ", str(e))

    return render(request, "auth/login.html", context=context)

def signup_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_model = get_user_model()
        user_obj = user_model.objects.create_user(username=username)
        user_obj.set_password(password)
        user_obj.save()
        user_auth = authenticate(username=username, password=password)
        login(request, user_auth)
        # return render(request, "home.html")
        return redirect(reverse('home_view'))
    else:
        return render(request, 'auth/signup.html')


def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            passo = form.cleaned_data['new_password1']
            print("passo= ", passo)
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            # gonullu passwordunu değiştirmeye gerek yok
            messages.success(request, 'Parolanız başarıyla değiştirildi!')
            return redirect(reverse('home_view'))
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'auth/change_password.html', {
        'form': form
    })
