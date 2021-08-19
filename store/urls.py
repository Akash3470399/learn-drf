from django.urls import path
from .import views

urlpatterns = [
    path('',views.StoreList.as_view(), name='store-list'),
    path('<str:pk>/', views.StoreView.as_view(), name='store-detail'),
]
