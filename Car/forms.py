from django import forms
from .models import CarModel,Comment

class CarForm(forms.ModelForm):
    class Meta:
        model = CarModel
        exclude= ['buyer']
        
class CommentForms(forms.ModelForm):
    class Meta:
        model = Comment
        fields= ['name','email','body']