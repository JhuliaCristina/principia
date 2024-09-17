from django.contrib.auth import login, get_user_model, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from .models import UserProfile 
from .forms import CustomUserCreationForm

def vendor_details(request,pk):
    user = User.objects.get(pk=pk)

    return render(request,'userprofile/vendor_details.html', {'user' :user})

@login_required
def minha_conta(request):
    return render(request, 'userprofile/minhaconta.html')

def minha_loja(request):
    return render(request, 'userprofile/minhaloja.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid(): 
            user = form.save()
            UserProfile.objects.create(user=user)
            login(request, user)
            return redirect('minhaconta') 
  # Redireciona para a página de login após o registro
    else:
        form = UserCreationForm()
    return render(request, 'userprofile/register.html', {'form': form})


@login_required
def logout(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Finaliza a sessão do usuário atual
            logout(request,user)

            # Cria o perfil de usuário associado ao usuário recém-criado
            userprofile = UserProfile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/logout.html', {'form': form})


@login_required
def update_profile(request):
    user = request.user
    userprofile = user.userprofile

    if request.method == 'POST':
        form = UserCreationForm(request.POST, instance=user)

        if form.is_valid():
            user = form.save()  # Atualiza o usuário

            # Atualiza os campos do UserProfile
            userprofile.username = request.POST.get('username')
            userprofile.password = request.POST.get('password')  # Se for plain-text
            userprofile.save()

            return redirect('login')  # Redireciona após atualizar
    else:
        # Preenche o formulário com os dados atuais do usuário e perfil
        form = UserCreationForm(instance=user)
        initial_data = {
            'username': userprofile.username,
            'password': userprofile.password,
        }

    return render(request, 'userprofile/update_profile.html', {
        'form': form,
        'username': userprofile.username,  # Para preencher o campo no template
        'password': userprofile.password,  # Para preencher o campo no template (não é recomendado exibir senhas)
    })

@login_required
def delete_profile(request):
    user = request.user

    if request.method == 'POST':
        if request.POST.get('confirm') == 'yes':
            userprofile = user.userprofile
            user.delete()  # Exclui o usuário
            userprofile.delete()  # Exclui o perfil associado
            auth_logout(request)  # Finaliza a sessão do usuário após a exclusão
            return redirect('frontpage')  # Redireciona para a página principal após deletar

    return render(request, 'userprofile/delete_profile.html')