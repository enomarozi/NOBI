from django import forms
from .models import KelolaFAQ

class CustomFormFAQ(forms.ModelForm):
	pertanyaan = forms.CharField(label="Pertanyaan", max_length=255, widget=forms.TextInput(attrs={"class":"form-control"}))
	jawaban = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':10, 'cols':40,'style': 'height: 200px; width: 100%;'}))

	class Meta:
		model = KelolaFAQ
		fields = ["pertanyaan","jawaban"]
