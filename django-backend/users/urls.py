from django.urls import path, re_path
from dj_rest_auth.registration.views import RegisterView, VerifyEmailView, ConfirmEmailView, ResendEmailVerificationView
from dj_rest_auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.UserList.as_view()),
    path('<int:pk>', views.UserDetail.as_view()),
    path('<int:pk>/subscribe', views.Subscribe.as_view()),
    path('account-confirm-email/<str:key>/', ConfirmEmailView.as_view()),
    path('resend-email/', ResendEmailVerificationView.as_view()),
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),

    path('verify-email/',
         VerifyEmailView.as_view(), name='rest_verify_email'),
    path('account-confirm-email/',
         VerifyEmailView.as_view(), name='account_email_verification_sent'),
    re_path(r'^account-confirm-email/(?P<key>[-:\w]+)/$',
            VerifyEmailView.as_view(), name='account_confirm_email'),
]
