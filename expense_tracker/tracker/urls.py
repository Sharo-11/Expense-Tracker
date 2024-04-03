from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('enter-Income/', enter_Income, name = "enter_Income"),
    path('enter-expense/', enter_Expense, name = 'enter_Expense'),
    path('', dashboard, name = 'dashboard'),
]
