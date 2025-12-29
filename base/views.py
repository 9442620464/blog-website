from django.shortcuts import render,redirect
from django.http import HttpResponse
from base.models import Category,Articles
from django.contrib.auth.forms import AuthenticationForm
from base.forms import RegistrationFrom
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    
    article=Articles.objects.filter(status='published',is_trending=True).order_by('-updated_on')
    not_trend_article=Articles.objects.filter(status='published',is_trending=False)
    
    content={
        
        'articles':article,
        'not_trend_article':not_trend_article

    }
    return render(request,'home.html',content)

def category_articals(request,cat):
    
    key=Category.objects.get(category_name=cat)

    context={
        
        'articles':Articles.objects.filter(Category=key.id),
        'category':key
    }
    return render(request,'category.html',context)

@login_required(login_url='login page')
def single_artical(request,info):

    context={
        'article':Articles.objects.get(slug=info)
    }

    return render(request,'single_artical.html',context)


def register(request):
    if request.method=="POST":
        form=RegistrationFrom(request.POST)
        context={
            'form':form
        }

        if form.is_valid():
            form.save()
            return redirect('login page')
            
        else:
            return render(request,'register.html',context)
            
            
    form=RegistrationFrom()
    context={
        'form':form
    }
    return render(request,'register.html',context)


def user_login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        # print(request.POST)
        # print(request)
        # print(form)
        
       
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('home')
        else:
         
            
            return render(request,'login.html',{'form':form})
    form=AuthenticationForm()
    context={
        'form':form
    }
    return render(request,'login.html',context)

def user_logout(request):
    auth.logout(request)
    return redirect('home')
