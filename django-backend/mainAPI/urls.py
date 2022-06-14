from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.test, name='test'),
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
]