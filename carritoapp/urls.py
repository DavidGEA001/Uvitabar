from django.urls import path
from . import views

urlpatterns = [
    path('carrito/', views.pagina_carrito, name= "carrito"),
    path('agregar/<int:article_id>', views.agregar_producto, name = "Add"),
    path('eliminar/<int:article_id>', views.eliminar_producto, name = "Delete"),
    path('restar/<int:article_id>', views.restar_producto, name = "Sub"),
    path('limpiar/', views.limpiar_carrito, name = "Clear"),

]
