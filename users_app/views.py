from django.shortcuts import render, redirect
from .models import User

# Create your views here.

def index(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'index.html', context)

def add_user(request):
    if request.method == "POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email_address=request.POST['email_address']
        age=request.POST['age']
        User.objects.create(first_name=first_name, last_name=last_name, email_address=email_address, age=age)
    return redirect('/')

def delete_user(request, id):
    print('USER TO DELETE: ', id)
    user_to_delete = User.objects.get(id=id)
    if user_to_delete:
        user_to_delete.delete()
    return redirect('/')
