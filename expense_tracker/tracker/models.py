from django.db import models

class Income(models.Model):
    amount  = models.DecimalField(max_digits = 10, decimal_places = 2)

class Expense(models.Model):
    amount = models.DecimalField(max_digits = 10, decimal_places = 2)
    description = models.CharField(max_length = 100)
    date = models.DateField(auto_now_add = True)

class Record(models.Model):
    income = models.ForeignKey(Income, on_delete = models.CASCADE)
    expense = models.ForeignKey(Expense, on_delete = models.CASCADE)
    available_balance = models.DecimalField(max_digits=15, decimal_places = 2)