from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Product, AdvUser, Order


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ("name", "desc", "photo")


class RegisterForm(UserCreationForm):
    class Meta:
        model = AdvUser
        fields = ("username", "password1", "password2", "photo")
        help_texts = {
            'username': None,
            'password1': None,
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        for field_name in ('username', 'password1', "password2", 'photo'):
            self.fields[field_name].help_text = ''


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = "__all__"
        widgets = {'user': forms.HiddenInput, 'product': forms.HiddenInput}
