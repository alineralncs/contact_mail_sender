from django.shortcuts import render
from django.contrib import messages
from .forms import ContatoForm

# Create your views here.
def contato(request):
    if str(request.method) == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.send_email()
            print('mandar?')
            messages.success(request, "Email enviado com sucesso :)")
            form = ContatoForm()
        else:
            print('nao?')
            messages.error(request, "Não foi possivel")
    else:
        form = ContatoForm()
    context = {
            "form": form
    }
    return render(request, "contato.html", context)