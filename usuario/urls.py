from django.urls import path
from .views import UsuarioCreate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('registrar/', UsuarioCreate.as_view(), name='registrar'),
     path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
     path('logout/', auth_views.LogoutView.as_view(), name='logout')
]