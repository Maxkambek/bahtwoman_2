from django.urls import path
from . import views

urlpatterns = [
    path('register-test/', views.RegisterTestListAPIView.as_view()),
    path('main-test/', views.MainTestListAPIView.as_view()),
    path('main-test-check/', views.MainTestCheck.as_view()),
    path('questions/', views.QuestionListAPIView.as_view()),
    path('questions/<int:pk>/', views.QuestionRetrieveAPIView.as_view())
]
