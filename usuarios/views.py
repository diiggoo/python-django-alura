from django.shortcuts import render, redirect
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    form = LoginForms()

    if request.method == 'POST':
        form = LoginForms(request.POST)

        if form.is_valid():
            nome_login=form["nome_login"].value()
            senha=form["senha"].value()

        usuario = auth.authenticate(
            request,
            username=nome_login,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome_login} logado com sucesso')
            return redirect('index')
        else:
            messages.error(request, 'Erro ao efetuar login')
            return redirect('login')


    return render(request, 'usuarios/login.html', {"form" : form})

def cadastro(request):
    form = CadastroForms()
    pass_fields = ["senha", "confirma_senha"]

    if request.method == 'POST':
        form = CadastroForms(request.POST)
        
        if form.is_valid():

            nome=form["nome_cadastro"].value()
            email=form["email"].value()
            senha=form["senha"].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request, 'Usuário já cadastrado. Tente outro nome')
                return redirect('cadastro')
            
            usuario=User.objects.create_user(
                username=nome,
                email=email,
                password=senha
            )
            usuario.save()
            messages.success(request, 'Cadastrado com sucesso')
            return redirect("login")

    return render(request, 'usuarios/cadastro.html', {"form" : form, "pass_fields": pass_fields})

def logout(request):
    auth.logout(request)
    messages.success(request, "Logout efetuado com sucesso")
    return redirect('login')