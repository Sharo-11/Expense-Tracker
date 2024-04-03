from django.shortcuts import render, redirect
from .forms import *
from .models import *

def enter_Income(request): 
    if request.method == "POST":
        form = IncomeForm(request.POST)
        if form.is_valid():
            income = form.save()
            record = Record.objects.create(income = income, available_balance = income.amount)
            return redirect('dashboard')
    else:
        form = IncomeForm()
        return render(request, 'enter_Income.html', {'form'  : form})
    
def enter_Expense(request):
    if request.method == "POST":
        form = ExpenseFrom(request.POST)
        if form.is_valid():
            expense = form.save()
            latest_record = Record.objects.latest("id")
            available_balance = latest_record.available_balance - expense.amount
            record = Record.objects.create(income=latest_record.income, expense=expense, available_balance=available_balance)
            return redirect('dashboard')
    else:
        form = ExpenseFrom()
    
    return render(request, 'enter_Expense.html', {'form': form})

        
def dashboard(request):
    records = Record.objects.all()
    return render(request, 'dashboard.html', {'records' : records})