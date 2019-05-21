from django.shortcuts import render,get_object_or_404,redirect
from .models import Meal, Order
from .forms import MealForm, OrderForm

# Create your views here.
def home(request):
    posts_meal = Meal.objects.all()
    context={
        'posts_meal':posts_meal,
    }
    return render(request, 'order_list/index.html', context)


def meal_detail(request, post_id):
    details = get_object_or_404(Meal, pk=post_id)
    context={
        'details':details,
    }
    return render(request, 'order_list/detail.html',context)

def add_meal(request):
    if request.method == 'POST':
        form = MealForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return  redirect('/index')
    else:
        form = MealForm()
    context = {
        'form': form
    }
    return render(request, 'order_list/meal_add.html', context)

def order_form(request):
    orders = Order.objects.filter()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.user = request.user
            new_form.save()
            return  redirect('/success')
    else:
        form = OrderForm()
    context = {
        'form': form,
        'orders':orders,
    }
    return render(request, 'order_list/orderForm.html', context)

 
