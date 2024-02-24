from django.urls import path
from . import views

urlpatterns =[
    path('dashboard', views.index, name='index'),
    path('personal/', views.personal, name='personal'),
    path('personal/detalles/<int:pk>/', views.detalles_staff, name='detalles_staff'),
    path('producto/', views.producto, name='productos'),
    path('pedido/', views.pedido, name='pedido'),
    path('producto/eliminar/<int:pk>/', views.eliminar_producto, name='eliminar_producto'),
    path('producto/actualizar/<int:pk>/', views.actualizar_producto, name='actualizar_producto')
]