from django import forms
from .models import Meal,Order

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name_meal', 'content', 'image','price']



class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['name','phon_number', 'email','location', 'Number_of_meal',]