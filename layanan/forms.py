from django import forms
from .models import KelolaLayanan

class CustomFormLayanan(forms.ModelForm):
	title = forms.CharField(label="Judul", max_length=20, widget=forms.TextInput(attrs={"class":"form-control"}))
	content = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control','row':10, 'cols':40,'style': 'height: 200px; width: 100%;'}))

	class Meta:
		model = KelolaLayanan
		fields = ["title","content"]
