from django.urls import path
from .import views

urlpatterns = [
    path('store/',views.StoreList.as_view(), name='store-list'),
    path('store/<str:pk>/', views.StoreView.as_view(), name='store-detail'),

]
