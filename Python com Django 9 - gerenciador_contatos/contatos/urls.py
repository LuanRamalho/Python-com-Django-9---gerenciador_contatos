from django.urls import path
from .views import listar_contatos, adicionar_contato, editar_contato, excluir_contato

urlpatterns = [
    path('', listar_contatos, name='listar_contatos'),
    path('adicionar/', adicionar_contato, name='adicionar_contato'),
    path('editar/<int:id>/', editar_contato, name='editar_contato'),
    path('excluir/<int:id>/', excluir_contato, name='excluir_contato'),
]
