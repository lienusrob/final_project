from django.urls import path, include
from .views import HomeView, SignUp
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path ('', HomeView.as_view(), name = 'homepage'),
    path('signup', SignUp.as_view(template_name = 'registration/signup.html'), name='signup'),
    path('login', auth_views.LoginView.as_view(template_name = 'registration/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(next_page = 'homepage'), name = 'logout'),
    #path ('profile_list/', UserListView.as_view(template_name = 'registration/profile_list.html'), name= 'profile_list'),

]
