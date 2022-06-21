from django.urls import path
from videos import views

urlpatterns = [
    path('', views.VideoList.as_view()),
    path('<int:pk>', views.VideoDetail.as_view()),
    path('<int:pk>/likes', views.LikesDetail.as_view()),
    path('<int:pk>/comment', views.CommentView.as_view()),
]
