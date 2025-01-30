from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class CustomSigninForm(AuthenticationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields["username"].widget.attrs.update({"class":"form-control","max-length":30,"value":"administrator","required":True})
		self.fields["password"].widget.attrs.update({"class":"form-control","max-length":30,"value":"12345678","required":True})


class CustomSignupForm(forms.ModelForm):
	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={"class":"form-control"}))
	email = forms.EmailField(label="Email", max_length=100, widget=forms.EmailInput(attrs={"class":"form-control"}))
	password1 = forms.CharField(label="Password" ,max_length=30, widget=forms.PasswordInput(attrs={"class":"form-control"}))
	password2 = forms.CharField(label="Konfirm Password", max_length=30, widget=forms.PasswordInput(attrs={"class":"form-control"}))

	class Meta:
		model = User
		fields = ["username","email","password1","password2"]

class CustomProfileForm(forms.ModelForm):
	firstname = forms.CharField(label="Firstname", max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
	lastname = forms.CharField(label="Lastname", max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
	username = forms.CharField(label="Username", max_length=30, widget=forms.TextInput(attrs={"class":"form-control"}))
	email = forms.EmailField(label="Email", max_length=40, widget=forms.EmailInput(attrs={"class":"form-control"}))
	is_superuser = forms.CharField(label="Is Superuser", max_length=15, widget=forms.TextInput(attrs={"class":"form-control"}))

	class Meta:
		model = User
		fields = ["firstname","lastname","username","email","is_superuser"]