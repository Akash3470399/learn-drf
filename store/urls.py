from django.urls import path
from .import views

urlpatterns = [
    path('',views.StoreList.as_view()),
    path('<str:pk>/', views.StoreView.as_view()),
]
