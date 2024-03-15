from django.shortcuts import render,redirect
from .models import List
from .forms import ListForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout

def land(request):
    return render(request,'landing_page.html')


def home(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)
        
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return HttpResponseRedirect(request.path_info)
    all_items = List.objects.filter(user=request.user)
    
    return render(request, 'home.html', {'all_items': all_items})

 
def delete(request,list_id):
    item=List.objects.get(pk=list_id)
    item.delete()
    messages.success(request,("Item deleted!"))
    return redirect('home')

def cross_off(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=True
    item.save()
    messages.success(request,("Item Crossed!"))
    return redirect('home')

def cross_on(request,list_id):
    item=List.objects.get(pk=list_id)
    item.completed=False
    item.save()
    messages.success(request,("Item Uncrossed!"))
    return redirect('home')

def edit(request,list_id):
    if request.method=='POST':
        item=List.objects.get(pk=list_id)
        form = ListForm(request.POST or None,instance=item)
        
        if form.is_valid():
            form.save()
            messages.success(request,("Item Edited!"))
            return redirect('home')
    
    else:    
        item = List.objects.get(pk=list_id)
        return render(request,'edit.html',{'item':item})
    
def login_page(request):
    
    if request.method == 'POST':
        email =request.POST.get('email')
        password =request.POST.get('password')
        user_obj = User.objects.filter(username=email)           
        user_obj = authenticate(username=email, password=password)
        try:
            if user_obj is not None:
                login(request,user_obj)
                return redirect('home')
            else:
                return redirect('login')
        except Exception as e:
            print(e)   
    
    
    return render(request,'login_page.html')

def register_page(request):
    if request.method == 'POST':
        first_name =request.POST.get('first_name')
        email =request.POST.get('email')
        password =request.POST.get('password')

        user_obj = User.objects.filter(username=email)
        
        if user_obj.exists():
            messages.warning(request,"Email already taken")
            return HttpResponseRedirect(request.path_info)
        else:
            user_obj = User.objects.create(first_name=first_name,email = email, username=email)
            user_obj.set_password(password)
            user_obj.save()
            messages.warning(request,"Account Created")
            return redirect('landing_page')
        
    return render(request,'login_page.html')

def log_out(request):
    logout(request)
    return redirect('landing_page')

