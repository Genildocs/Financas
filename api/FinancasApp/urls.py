from django.urls import path
from . import views

urlpatterns = [
    path('financas/', views.financasApi),
    path('compras/', views.ComprasApi),

]