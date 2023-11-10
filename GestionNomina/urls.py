from django.urls import path
from . import views
from .views import DepartamentoListView
from .views import listar_empleados
urlpatterns = [
    path('', views.BASE,name='BASE' ),
    path('Contactos/', views.CONTACTO,name='CONTACTO' ),
    # --------------------model Departamento ---------------------------------
    path('departamentos/', DepartamentoListView.as_view(),name='departamento_list'),
    path('crearDepartamento/', views.crearDepartamento),
    path('detalleDepartamento/detalle/<int:pk>/', views.detalleDepartamento, name='detalleDepartamento'),
    path('edicionDepartamento/edicion/<int:pk>/', views.edicionDepartamento, name='edicionDepartamento'),
    path('editarDepartamento/editar/<int:pk>/', views.editarDepartamento, name='editarDepartamento'),
    # ------------------Inicio Del Model Cargo--------------------------------
    path('cargo', views.listar_cargos, name='listar_cargos'),
    path('departamento/', views.get_departamento, name='get_departamento'),
    path('crearCargo/', views.crearCargo, name='crearCargo'),
    path('editarCargo/editar<int:cargo_id>/', views.editarCargo, name='editarCargo'),
    path('edicionCargo/edicion/<int:cargo_id>/', views.edicionCargo, name='edicionCargo'),
    path('detalleCargo/detalle/<int:cargo_id>/', views.detalleCargo, name='detalleCargo'),

    # ------------------Inicio Del Model Departamento--------------------------------
    path('empleado', views.listar_empleados, name='listar_empleados'),
]
