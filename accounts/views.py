from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.db import connection
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import CustomSigninForm, CustomSignupForm
from datetime import datetime

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
				return HttpResponseRedirect(reverse('dashboard'))
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
					return HttpResponseRedirect(reverse('dashboard'))
				else:
					messages.error(request, "Pendaftaran Gagal", "Password Tidak Sama dengan Konfirmasi Password.")
			else:
				messages.error(request, "Pendaftaran Gagal, Panjang Password minimal 8 Karakter.")
		else:
			messages.error(request, "Pendaftaran Gagal, Pastikan lagi Inputannya.")

	return render(request, 'account/signup.html', {'form':form, 'context':context})

def profile(request):
	if request.user.is_authenticated:
		auth = request.user.username
		user = User.objects.get(username=auth)
		if request.method == "POST":
			user = get_object_or_404(User, id=request.POST.get('id'))
			user.first_name = request.POST.get('firstname')
			user.last_name = request.POST.get('lastname')
			user.username = request.POST.get('username')
			user.email = request.POST.get('email')
			user.is_superuser = request.POST.get('is_superuser')
			user.save()
		return render(request, 'account/profile.html',{'user':user})
	return HttpResponseRedirect(reverse('signin'))

def setting(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			password_sekarang = request.POST.get('password_sekarang')
			password_baru1 = request.POST.get('password_baru1')
			password_baru2 = request.POST.get('password_baru2')
			user = request.user
			if user.check_password(password_sekarang):
				if len(password_baru1) >= 8 and len(password_baru2) >= 8:
					if password_baru1 == password_baru2:
						if password_sekarang != password_baru2:
							user.set_password(password_baru2)
							user.save()
							update_session_auth_hash(request, user)
							messages.success(request, "Ganti Password Berhasil.")
							return HttpResponseRedirect(reverse('setting'))
						else:
							messages.error(request, "Ganti Password Gagal, Password Baru Anda Sama Dengan Sebelumnya.")
					else:
						messages.error(request, "Ganti Password Gagal, Password Baru dan Konfirmasi Password Tidak Sama.")
				else:
					messages.error(request, "Ganti Password Gagal, Panjang Password minimal 8 Karakter.")
			else:
				messages.error(request, "Ganti Password Gagal, Password Lama Salah.")
		return render(request,'account/setting.html')
	return HttpResponseRedirect(reverse('signin'))

def signout(request):
	if request.user.is_authenticated:
		logout(request)
	return HttpResponseRedirect(reverse('signin'))