from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView, name="index"),
    path('single_post/<int:id>', views.getSingle, name="single"),
    path('login_page', views.loginSys, name="login"),
    path('category_page', views.category, name="category"),
    path('logout', views.getLogout, name='logout'),
    path('register_page', views.registerUser, name="register")
    # path('profile_page', views.profileAuth, 'profile'),
]
