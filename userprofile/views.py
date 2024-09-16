from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.utils.text import slugify
from .models import Userprofile 

def vendor_details(request,pk):
    user = User.objects.get(pk=pk)

    return render(request,'userprofile/vendor_details.html', {'user' :user})

@login_required
def minha_conta(request):
    return render(request, 'userprofile/minhaconta.html')

def minha_loja(request):
    return render(request, 'userprofile/minhaloja.html')

@login_required
def register(request):
    if request.method== 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request,user) 
            userprofile = Userprofile.objects.create(user=user)

            return redirect('frontpage')
    
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
            userprofile = Userprofile.objects.create(user=user)

            return redirect('frontpage')
    else:
        form = UserCreationForm()

    return render(request, 'userprofile/logout.html', {'form': form})
