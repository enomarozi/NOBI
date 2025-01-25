from django import forms

class CustomFormMobil(forms.Form):
	merek = forms.CharField(label="Merek Mobil", max_length=30, widget=forms.TextInput(attrs={"class":"form-control"}))
	kapasitas = forms.IntegerField(label="Kapasitas", min_value=1, max_value=10, widget=forms.NumberInput(attrs={"class":"form-control"}))
	durasi = forms.ChoiceField(label="Durasi",
		choices=[
			('Harian','Harian'),
			('Mingguan','Mingguan'),
			('Bulanan','Bulanan'),
		],
		widget=forms.Select(attrs={"class":"form-control"}))
	harga = forms.CharField(label="Harga", widget=forms.TextInput(attrs={"class":"form-control"}))