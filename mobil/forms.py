from django import forms
from .models import KelolaMobil
from django.core.validators import FileExtensionValidator
from django.core.exceptions import ValidationError

def validate_file_size(value):
	limit = 10 * 1024 * 1024
	if value.size > limit:
		raise ValidationError("File terlalu besar. Maksimal 10MB.")

class CustomFormMobil(forms.ModelForm):
	filename = forms.FileField(required=True, widget=forms.ClearableFileInput(attrs={'class': 'form-control'}),validators=[ FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg', 'bmp']), validate_file_size])
	merek = forms.CharField(label="Merek Mobil", max_length=30, widget=forms.TextInput(attrs={"class":"form-control"}))
	kapasitas = forms.IntegerField(label="Kapasitas", min_value=1, max_value=50, widget=forms.NumberInput(attrs={"class":"form-control"}))
	durasi = forms.ChoiceField(label="Durasi",
		choices=[
			('Harian','Harian'),
			('Mingguan','Mingguan'),
			('Bulanan','Bulanan'),
		],
		widget=forms.Select(attrs={"class":"form-control"}))
	harga = forms.CharField(label="Harga", widget=forms.TextInput(attrs={"class":"form-control"}))

	class Meta:
		model = KelolaMobil
		fields = ["filename","merek","kapasitas","durasi","harga"]