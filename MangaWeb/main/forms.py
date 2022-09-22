from dataclasses import field, fields
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from main.models import BLOG, REVIEW



class ContactForm(forms.ModelForm):

	name = forms.CharField(max_length=100, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '*Full name..',
			}))
	email = forms.EmailField(max_length=254, required=True, 
		widget=forms.TextInput(attrs={
			'placeholder': '*Email..',
			}))
	message = forms.CharField(max_length=1000, required=True, 
		widget=forms.Textarea(attrs={
			'placeholder': '*Message..',
			'rows': 6,
			}))


	class Meta:
		fields = ('name', 'email', 'message',)

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class BlogForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '',
			}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '',
			}))
	body = forms.CharField(max_length=1000, required=True,
		widget=forms.Textarea(attrs={
			'placeholder': '',
			}))
	image = forms.ImageField()


	class Meta:
		model = BLOG
		fields = ['author','name','description','body','image']


class ReviewForm(forms.ModelForm):

	author = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '',
			}))
	name = forms.CharField(max_length=200, required=True,
		widget=forms.TextInput(attrs={
			'placeholder': '',
			}))
	body = forms.CharField(max_length=1000, required=True,
		widget=forms.Textarea(attrs={
			'placeholder': '',
			}))
	image = forms.ImageField()


	class Meta:
		model = REVIEW
		fields = ['author','name','description','body','image']


#Crea los Formularios ya existentes de DJANGO forms, usa la clase Meta y pide los atributos que quieras que tengamos existentes de los modelos (en este caso REVIEW y BLOG)