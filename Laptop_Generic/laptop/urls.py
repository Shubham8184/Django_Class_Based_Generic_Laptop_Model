from django.urls import path
from .views import HomeView, LaptopCreateView, LaptopUpadteView, LaptopdeleteView, Laptoplistview


urlpatterns=[
    path('home/',HomeView.as_view(),name='home'),
    path('show/',Laptoplistview.as_view(),name='show'),
    path('add/',LaptopCreateView.as_view(),name='add'),
    path('update/<int:pk>',LaptopUpadteView.as_view(),name='update'),
    path('delete/<int:pk>',LaptopdeleteView.as_view(),name='delete'),

]