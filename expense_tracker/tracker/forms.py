from django import forms
from  .models import *

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount']
        lables = {
            'amount' : 'Amount'
        } 
        widgets = {
            'amount' : forms.NumberInput(attrs = {'step' : '0.01'})
        }

class ExpenseFrom(forms.ModelForm):
    class Meta:
        model = Expense
        fields =  ['amount', 'description']
        lables = {
            'amount' : "Amount",
            'description' : "Description"
        }
        widgets = {
            'amount' : forms.NumberInput(attrs = {'step' : '0.01'}),
            'description' : forms.TextInput(attrs = {'placeholder' : 'Enter Description'})
        }