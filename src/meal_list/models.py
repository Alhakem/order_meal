from django.db import models
from django.utils import timezone
import datetime
 
# Create your models here.
class Meal(models.Model):
    name_meal = models.CharField(max_length=100,verbose_name='اسم الوجبة',null=True, blank=True)
    content = models.TextField(verbose_name='وصف الوجبة')
    image = models.URLField( null= True)
    price = models.DecimalField(max_digits=10, decimal_places=2,verbose_name='سعر الوجبة')
    post_date = models.DateTimeField(default= timezone.now)
    post_update = models.DateTimeField(blank=True, default=datetime.datetime.now)
     
   
    def __str__(self):
        return self.name_meal
    
class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name='الاسم')
    email = models.EmailField(verbose_name='البريد الالكتروني')
    phon_number = models.IntegerField(blank=True,verbose_name='رقم الهاتف ')
    location = models.CharField(max_length=100,verbose_name='العنوان')
    Number_of_meal = models.IntegerField(default=1,verbose_name='عدد الوجبة')
    order_date = models.DateTimeField(auto_now_add = True)
    order = models.ForeignKey(Meal, on_delete=models.CASCADE, related_name='orders',null=True, blank=True)
    
   
    def __str__(self):
        return '{}'" طلب هذه الوجبة "' {}'.format(self.name , self.order)
    class Meta:
        ordering = ['-order_date']