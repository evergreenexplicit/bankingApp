from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db.models import Q
from .forms import RegisterForm, TransactionForm
from .models import Transaction,BankUser

def index(request):
    return render(request, "index.html")
def menu(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(
        request,
        "menu.html",
        context={
            'transactions':Transaction.objects.filter(
                Q(sender=request.user.bankuser) 
                | Q(receiver=request.user.bankuser)
            ).order_by("-date")
        })


    



def new_transaction(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            if len(User.objects.filter(username=request.POST['receiver'])) < 1 or int(request.POST['moneyValue']) < 0 :
                return render(request, "error_transaction.html", {'error': 'Wrong transaction receiver.'})
            return render(request, 'confirm_transaction.html', {'transaction': form.cleaned_data})
            
    else:
        form = TransactionForm()
    return render(request, 'new_transaction.html', {'form': form})
    

def confirm_transaction(request):
    print("XDD")
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        print(request.POST)
        receiver = request.POST['receiver']
        moneyValue = int(request.POST['moneyValue'])
        Transaction.objects.create(
            sender=request.user.bankuser,
            receiver = User.objects.filter(username=receiver)[0].bankuser,
            moneyValue = moneyValue
        )
        return render(request,'confirmed_transaction.html',context={
            'receiver':receiver,
            'moneyValue':moneyValue
        })
'''
def confirmed_transaction(request):
    if not request.user.is_authenticated:
        return redirect('/')
    form = TransactionFormRO()
'''

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/menu')
    else:
        form = RegisterForm()

    
    return render(request, 'register.html', {'form': form})
    
# Create your views here.
'''


    def new_transaction(request):
    if not request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            Transaction.objects.create(
                sender=request.user.bankuser,
                receiver = User.objects.filter(username=request.POST['receiver'])[0].bankuser,
                moneyValue = int(request.POST.get('moneyValue',0))
            )
        #else:
            #TODO invalid transa tion
    else:
        form = TransactionForm()
    return render(request, 'new_transaction.html', {'form': form})
    
'''