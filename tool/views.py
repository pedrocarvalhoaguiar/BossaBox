from django.shortcuts import render, get_object_or_404
from .models import Tool
from django.core.paginator import Paginator


def index(request):
    tools = Tool.objects.order_by('-id')
    return render(request, 'index.html', {'tools': tools})


def ver_tool(request):
    pass


def criar_tool(request):
    pass


def buscar_tool(request):
    pass