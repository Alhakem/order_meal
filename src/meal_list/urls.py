from django.urls import path
from . import views 


urlpatterns = [
    path("", views.home, name='home'),
    path("detail/<int:meal_id>/", views.meal_detail, name='details'),
    path('add_meal', views.add_meal, name='add_meals'),
    path('<int:meal_id>/update$', views.update_meal, name='edit_meals'),
    path('^detail/<int:meal_id>/order_Form$',views.order_form, name='order_Forms'),
    path("list_order", views.list_order, name='list_order'),
    path("success-order", views.success_order, name='success-order'),
     
]