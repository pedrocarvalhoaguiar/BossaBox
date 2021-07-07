from django.urls import path
from . import views


urlpatterns = [
    path('tool/int:<tool_id>', views.delete_tool, name='delete_tool'),
    path('', views.index, name='index'),
    path('busca/', views.buscar_tool, name='buscar_tool'),
]