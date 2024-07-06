from django.urls import path,include
from .import views
urlpatterns = [
   path("signup/", views.SignUp, name="signup"),
   path("login/", views.Userlogin.as_view(), name="login"),
   path("profile/", views.profile, name="profile"),
   path("logout/", views.userlogout, name="logout"),
   path("profile/edit/", views.updateprofile, name="updateprofile"),
   path("profile/passchange", views.passchange, name="passchange"),
   path("buy/<int:id>", views.buy, name="buy_car"),
]