from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView, UpdateView, DeleteView

from apps.Clientes.forms import ClienteForm
from apps.Clientes.models import Cliente

# Create your views here.

def index(request):
    return HttpResponse("Pagina principal de app cliente")

def index(request):
    return render(request,'cliente/index.html')

def cliente_view(request):    
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
        return  redirect('cliente:cliente_listar')
    else:
        form = ClienteForm()
    return render(request,'cliente/cliente_form.html',{'form': form})    

def cliente_list(request):
    cliente = Cliente.objects.all().order_by('id')
    contexto = {'cliente' : cliente} 
    return render(request,'cliente/cliente_list.html',contexto)

class ClienteList(ListView):
    model = Cliente
    template_name = 'cliente/cliente_list.html'
    paginate_by = 10

class ClienteCreate(CreateView):    
    model = Cliente
    form_class = ClienteForm
    template_name = 'cliente/cliente_form.html'
    success_url = reverse_lazy('cliente:cliente_listar')

