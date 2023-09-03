from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverView, name='apiOverview'), #OBS:<int:pk> indica que é necessário usar o id do dado para realizar a ação
    path('product-list/',views.ShowAll, name='product-list'),
    path('product-detail/<int:pk>',views.ViewProduct, name='product-detail'),
    path('product-create/',views.CreateProduct, name="product-create"),
    path('product-update/<int:pk>',views.updateProduct, name="product-update"),
    path('product-delete/<int:pk>',views.deleteProduct, name="product-delete"),
]