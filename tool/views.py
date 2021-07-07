from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import FormTool
from django.core.paginator import Paginator
from .models import Tool
from django.db.models import Q


def index(request, search='empty'):
    if search == 'empty':
        tools = Tool.objects.order_by('-id')
    else:
        tools = search
    categorias = []
    for tool in tools:
        tags = tool.tags.split(' ')
        categorias.append(tags)
    paginator = Paginator(tools, 3)
    page = request.GET.get('p')
    tools = paginator.get_page(page)
    both = zip(tools, categorias)
    if request.method != 'POST':
        form = FormTool
        return render(request, 'index.html', {
            "both": both,
            'form': form,
            'tools': tools,
        })
    form = FormTool(request.POST)
    if form.is_valid():
        form.save()
        return redirect('index')


def delete_tool(request, tool_id):
    Tool.objects.get(pk=tool_id).delete()
    return redirect('index')


def buscar_tool(request):
    termo = request.GET.get('termo')
    tags_only = 'tags' in request.GET
    if tags_only:
        tools = Tool.objects.filter(tags__icontains=termo).order_by('-id')
    else:
        tools = Tool.objects.filter(Q(tags__icontains=termo) | Q(nome__icontains=termo))
    return index(request, search=tools)