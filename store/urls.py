from django.contrib.auth import views as auth_views
from django.urls import path
from .views import contact, detail, register

from .forms import LoginForm

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register , name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm) , name='login'),
    path('detail/<int:pk>/', detail, name='detail'),

]
