from django.shortcuts import render, redirect ,get_object_or_404
from .models import Login_user , Item
from django.contrib import messages
from django.contrib.auth.hashers import check_password , make_password
from .forms import ItemForm

# login_view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Verifica se o usuário existe no banco de dados
        user = Login_user.objects.filter(username=username).first()
        
        # Verifica se a senha está correta
        if user and check_password(password, user.password):
            request.session['user_id'] = user.id
            return redirect('home/lista')
         
         # Se o usuário não existir ou a senha estiver incorreta, exibe uma mensagem de erro
        messages.error(request, 'Invalid username or password')
        return redirect('login')
    return render(request, 'login/login.html')



# register_view
def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        # Verifica se as senhas coincidem
        if password1 != password2:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
        
        # Verifica se o usuário já existe no banco de dados
        if Login_user.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('register')
        
        # Cria o usuário no banco de dados
        Login_user.objects.create(username=username, password=make_password(password1))
        messages.success(request, 'Registration successful')
        return redirect('login')
    return render(request, 'login/register.html')


def register_item_view(request):
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista')
    else:
        form = ItemForm()
    return render(request, 'home/register_item.html', {'form': form})

def lista_view(request):
    user_id = request.session.get('user_id')
    user = None
    if user_id:
        user = Login_user.objects.filter(id=user_id).first()
    
    itens = Item.objects.all()
    return render(request, 'home/lista.html', {'itens': itens, 'usuario': user})



def deletar_item(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    item.delete()
    return redirect('lista')  



def favoritar_item(request):
    return render(request, 'home/fav.html')