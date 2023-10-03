from django.urls import path
from . import views
from .views import DepartamentoListView, DepartamentoCreateView,DepartamentoUpdateView,DepartamentoDeleteView

urlpatterns = [
    path('', views.BASE,name='BASE' ),
    path('departamentos/', DepartamentoListView.as_view(),name='departamento-list'),
    path('departamentos/crear/', DepartamentoCreateView.as_view(), name='departamento_create.html'),
    path('departamentos/editar/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('departamentos/eliminar/<int:pk>/', DepartamentoDeleteView.as_view(), name='departamento-delete'),
]
