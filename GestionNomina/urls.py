from django.urls import path
from . import views
from .views import DepartamentoListView, DepartamentoCreateView,DepartamentoUpdateView,DepartamentoDeleteView
from .views import CargoListView, CargoCreateView,CargoUpdateView,CargoDeleteView
urlpatterns = [
    path('', views.BASE,name='BASE' ),
    # --------------------model Departamento ---------------------------------
    path('departamentos/', DepartamentoListView.as_view(),name='departamento-list'),
    path('departamentos/crear/', DepartamentoCreateView.as_view(), name='departamento_create'),
    path('departamentos/editar/<int:pk>/', DepartamentoUpdateView.as_view(), name='departamento_update'),
    path('departamentos/eliminar/<int:pk>/', DepartamentoDeleteView.as_view(), name='departamento-delete'),

    # ------------------Inicio Del Model Cargo--------------------------------
    path('cargos/', CargoListView.as_view(),name='cargo_list'),
    path('cargos/crear/', CargoCreateView.as_view(), name='cargo_create'),
    path('cargos/editar/<int:pk>/', CargoUpdateView.as_view(), name='cargo_update'),
    path('cargos/eliminar/<int:pk>/', CargoDeleteView.as_view(), name='cargo_delete'),

]
