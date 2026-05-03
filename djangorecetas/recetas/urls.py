from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('ingredientes/', views.lista_ingredientes, name='lista_ingredientes'),
    path('ingredientes/nuevo/', views.crear_ingrediente, name='crear_ingrediente'),
    path('ingredientes/editar/<int:id>/', views.editar_ingrediente, name='editar_ingrediente'),
    path('ingredientes/eliminar/<int:id>/', views.eliminar_ingrediente, name='eliminar_ingrediente'),

    path('platos/', views.lista_platos, name='lista_platos'),
    path('platos/nuevo/', views.crear_plato, name='crear_plato'),
    path('platos/editar/<int:id>/', views.editar_plato, name='editar_plato'),
    path('platos/eliminar/<int:id>/', views.eliminar_plato, name='eliminar_plato'),

    path('menus/', views.lista_menus, name='lista_menus'),
    path('menus/nuevo/', views.crear_menu, name='crear_menu'),
    path('menus/editar/<int:id>/', views.editar_menu, name='editar_menu'),
    path('menus/eliminar/<int:id>/', views.eliminar_menu, name='eliminar_menu'),
] 