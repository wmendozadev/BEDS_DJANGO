
from django.conf.urls import url, include
from apps.Clientes.views import index, cliente_view, cliente_list,ClienteList,ClienteCreate

urlpatterns = [
     url(r'^index$', index, name='index'),
     #url(r'^nuevo$', ClienteCreate.as_view(), name='cliente_crear'),
     #url(r'^listar$', ClienteList.as_view(), name='cliente_listar'),
]

#url(r'^nuevo$', login_required(ClienteCreate.as_view()), name='cliente_crear'),
#url(r'^listar', login_required(ClienteList.as_view()), name='cliente_listar'),