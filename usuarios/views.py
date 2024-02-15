from django.shortcuts import render
from usuarios.forms import LoginForms, CadastroForms

def login(request):
    form = LoginForms()
    return render(request, 'usuarios/login.html', {"form" : form})

def cadastro(request):
    form = CadastroForms()
    pass_fields = ["senha", "confirma_senha"]
    return render(request, 'usuarios/cadastro.html', {"form" : form, "pass_fields": pass_fields})

def logout(request):
    pass