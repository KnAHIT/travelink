#coding=utf-8 
from django.shortcuts import render,render_to_response
from share.models import Account,Blog
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from share.forms import BlogForm
# Create your views here.

def home(request):
    blog_list = Blog.objects.all()
    
    if 'login' in request.GET:
        login_view(request)
    
    if 'logout' in request.GET:
        logout(request)
        
    user_is_login = False    
    if request.user is not None and request.user.is_active:
        user_now = request.user.username      
        user_is_login = True        
        
    if 'yj' in request.GET:
        author = Account.objects.get(Username=user_now)
        blog = Blog.objects.create(Username=author,Title=request.GET['yj_title'],
                                   Passage=request.GET['yj'])
        return HttpResponseRedirect("../../",locals())                        
    return render_to_response('index.html',locals())
    

def login_view(request):
    username = request.GET['username']
    password = request.GET['password']
    user = auth.authenticate(username=username, password=password)
    if user is not None and user.is_active:
        # Correct password, and the user is marked "active"
        auth.login(request, user)
        # Redirect to a success page.
        return HttpResponseRedirect("../../")
    else:
        # Show an error page
        return HttpResponseRedirect("/account/invalid/")



def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("../",locals())

def test_blog(request):
    if request.method == 'POST':
        blog_form = BlogForm(request.POST,request.FILES)
        if blog_form.is_valid():
            blog_form.save()
            return HttpResponse('image upload success')
    else:
        blog_form = BlogForm()
    blog ='http://127.0.0.1:8000/media/' + str(Blog.objects.get(id=16).Image)
    return render_to_response('testblog.html',locals())