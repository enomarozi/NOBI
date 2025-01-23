from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomSigninForm, CustomSignupForm
from datetime import datetime

def index(request):
	if request.user.is_authenticated:
		return render(request, 'admin/index.html')
	return HttpResponseRedirect(reverse('signin'))

def signin(request):
	context = {
		"title" : "SignIn Form"
	}
	if request.method == "POST":
		form = CustomSigninForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
		else:
			messages.error(request, "SignIn Failed, Pastikan lagi Inputannya.")
	else:
		form = CustomSigninForm()
	context['form'] = form
	return render(request, 'account/signin.html', context)

def signup(request):
	form = CustomSignupForm()
	context = {
		"title" : "SignUp Form",
	}
	if request.method == "POST":
		form = CustomSignupForm(data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			email = form.cleaned_data.get("email")
			password1 = form.cleaned_data.get("password1")
			password2 = form.cleaned_data.get("password2")
			today = datetime.today().date()
			if len(password1) >= 8 and len(password2) >= 8:
				if password1 == password2:
					user = User(username=username, email=email, date_joined=today)
					user.password = make_password(password2)
					user.save()
					messages.success(request, "Pendaftaran Berhasil, Silakan Coba Masuk.")
					return HttpResponseRedirect(reverse('index'))
				else:
					message.error(request, "Pendaftaran Gagal", "Password Tidak Sama dengan Konfirmasi Password.")
			else:
				messages.error(request, "Pendaftaran Gagal, Panjang Password minimal 8 Karakter.")
		else:
			messages.error(request, "Pendaftaran Gagal, Pastikan lagi Inputannya.")

	return render(request, 'account/signup.html', {'form':form, 'context':context})

def setting(request):
	return render(request, 'account/setting.html')
	
def signout(request):
	if request.user.is_authenticated:
		logout(request)
	return HttpResponseRedirect(reverse('signin'))