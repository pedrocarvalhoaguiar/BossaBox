from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tool/int:<tool_id>', views.ver_tool, name='ver_tool'),
    path('criar/', views.criar_tool, name='criar_tool'),
    path('busca/', views.buscar_tool, name='buscar_tool'),
]