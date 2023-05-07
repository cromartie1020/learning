from django.urls import path
from . import views
urlpatterns=[
    path('item_list', views.ItemList.as_view(), name='item_list'),
    path('item_detail/<int:pk>/', views.ItemDetail.as_view(), name='item_detail'),
    path('location_list', views.LocationList.as_view(), name='location_list'),
    path('location_detail/<int:pk>/', views.LocationDetail.as_view(), name='location_detail'),

]