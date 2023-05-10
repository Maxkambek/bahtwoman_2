from django.urls import path
from .views import LoginAPI, RegisterAPI, RegisterConfirmAPI, ChangePasswordAPI, UserAPI, ResetPasswordAPI, \
    ResetPasswordConfirmAPI, UserCardAPI, VerifyPhoneResetPasswordAPI, UserDetailsCreateAPIView

urlpatterns = [
    path('<int:pk>/', UserAPI.as_view()),
    path('login/', LoginAPI.as_view()),
    path('card/', UserCardAPI.as_view()),
    path('register/', RegisterAPI.as_view()),
    path('register-confirm/', RegisterConfirmAPI.as_view()),
    path('change-password/', ChangePasswordAPI.as_view()),
    path('reset-password/', ResetPasswordAPI.as_view()),
    path('verify-reset-password/', VerifyPhoneResetPasswordAPI.as_view()),
    path('confirm-reset-password/', ResetPasswordConfirmAPI.as_view()),
    path('register-question/', UserDetailsCreateAPIView.as_view()),
]
