from django.urls import path
from videos import views

urlpatterns = [
    path('', views.VideoList.as_view()),
    path('<int:pk>', views.VideoDetail.as_view()),
]
