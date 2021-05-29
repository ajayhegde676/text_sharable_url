from django.urls import path
from app import views


urlpatterns = [
    path('output/<int:pk>/', views.TextView.as_view(),name='result'),
    path('input/',views.InputView.as_view()),
]