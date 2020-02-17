from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm, Form
from django.contrib.auth.models import User

from .models import Transaction


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username',  'email', 'password1', 'password2',)

class TransactionForm(Form):
    receiver = forms.CharField(label='Receiver')
    moneyValue = forms.IntegerField(label='MoneyValue', min_value=0)
class TransactionFormRO(Form):
    receiver = forms.CharField(label='Receiver',widget=forms.TextInput(attrs={'readonly':'readonly'}))
    moneyValue = forms.IntegerField(label='MoneyValue', min_value=0,widget=forms.TextInput(attrs={'readonly':'readonly'}))