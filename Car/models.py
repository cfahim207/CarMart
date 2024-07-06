from django.db import models
from Brand.models import BrandModel
from django.contrib.auth.models import User

# Create your models here.
class CarModel(models.Model):
    name=models.CharField(max_length=100)
    discription=models.TextField()
    quantity=models.IntegerField()
    price=models.IntegerField()
    brand=models.ForeignKey(BrandModel,on_delete=models.CASCADE)
    image=models.ImageField(upload_to ='uploads/', blank=True, null= True)
    
    
    def __str__(self):
        return self.name
    
class Comment(models.Model):
    car=models.ForeignKey(CarModel,on_delete=models.CASCADE,related_name='comments')
    name=models.CharField(max_length=50)
    email=models.EmailField()
    body=models.TextField()
    created_on=models.DateTimeField(auto_now_add=True) #object creat hoyar sathe sathe date and time store hoye jabe
    
    
    def __str__(self):
        return f'comment by {self.name}'
    
