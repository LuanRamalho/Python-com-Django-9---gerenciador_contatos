from django.shortcuts import render, redirect, get_object_or_404
from .models import Contato
from .forms import ContatoForm

def listar_contatos(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/listar.html', {'contatos': contatos})

def adicionar_contato(request):
    if request.method == "POST":
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos')
    else:
        form = ContatoForm()
    return render(request, 'contatos/form.html', {'form': form})

def editar_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    if request.method == "POST":
        form = ContatoForm(request.POST, instance=contato)
        if form.is_valid():
            form.save()
            return redirect('listar_contatos')
    else:
        form = ContatoForm(instance=contato)
    return render(request, 'contatos/form.html', {'form': form})

def excluir_contato(request, id):
    contato = get_object_or_404(Contato, id=id)
    contato.delete()
    return redirect('listar_contatos')
