from django.urls import path
from . import views


urlpatterns = [
    path('tool/int:<tool_id>', views.ver_tool, name='ver_tool'),
    path('', views.index, name='index'),
    path('busca/', views.buscar_tool, name='buscar_tool'),
]