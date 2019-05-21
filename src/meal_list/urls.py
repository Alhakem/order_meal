from django.urls import path
from .views import home, meal_detail,add_meal,order_form
urlpatterns = [
    path("", home, name='home'),
    path("detail/<int:post_id>/", meal_detail, name='details'),
    path('add_meal', add_meal, name='add_meals'),
    path('detail/order_Form', order_form, name='order_Forms'),
]