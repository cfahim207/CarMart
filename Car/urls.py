
from django.urls import path,include
from .import views
urlpatterns = [
   path("details/<int:id>", views.Detailscar.as_view(), name="details_car")
]
