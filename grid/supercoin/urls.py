from django.urls import path
from . import views

urlpatterns = [ 
    path("", views.index),
    path("login", views.login,name="login"),
    path("signup", views.signup, name="signup"),
    path("customer", views.customer, name="customer"),
    path("seller", views.seller, name="seller"),
    path("admin", views.admin, name="admin"),
    path("customer/review", views.review, name="review"),
    path("seller/rewards", views.s_rewards, name="s_rewards"),
    path("customer/rewards", views.rewards, name="rewards"),
    path("customer/store", views.store, name="store"),
    path("customer/rewards/zara", views.zara, name="zara")
]

