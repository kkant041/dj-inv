from django.urls import path, include

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("signup", views.signupView, name="signup"),
    path("login", views.loginView, name="login"),
    path("allproducts", views.allProd, name="allProd"),
    path("addproduct", views.addProd, name="addProd"),
    path("remProd", views.remProd, name="remProd"),
    path("transactionhistory", views.transHisView, name="transHisView"),
]