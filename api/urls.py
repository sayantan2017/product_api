from django.urls import path
from .import views

urlpatterns = [
    path('product-list/',views.ShowAll,name='product-list'),
    path('product-details/<int:pk>/',views.viewproduct,name='product-details'),
    path('product-create/',views.createdata,name='product-create'),
    path('product-update/<int:pk>/',views.update,name='product-update'),
    path('product-delete/<int:pk>/',views.delete,name='product-delete')
]
