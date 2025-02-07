from django.shortcuts import render
from Car.models import CarModel
from Brand.models import BrandModel
def home(request, Brand_slug = None): # initially dhore nicchi je category_slug None thakbe karon hocche user first time home page e asle se normal page dekhbe, se filter korte chaile category te click korlei sei category er slug ta capture korbo ar seta tokhn ar None thakbe na
    
    data = CarModel.objects.all() # sob post gula ke niye aslam
    if Brand_slug is not None: # ekhn category slug jodi None na hoy tar mane sekhane value ache
        brand = BrandModel.objects.get(slug = Brand_slug) # slug je field model e likhechilam seta = amader category slug kore dilam taile ekhn kon category er slug sei category object peye jabo
        data = CarModel.objects.filter(brand  = brand) # post er category te category object bosiye filter korlam, ager data er sathe overright hoye jabe
    brands = BrandModel.objects.all() # sob category dekhabo
    return render(request, 'home.html', {'data' : data, 'brand' : brands})


