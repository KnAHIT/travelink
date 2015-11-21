#coding=utf-8 
from django.shortcuts import render,render_to_response
from share.models import Account,Blog,Diary,Travel_plan
from django.contrib import auth
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from share.forms import BlogForm,DiaryForm,AccountForm,PlanForm
# Create your views here.

def home(request):
    blog_list = Blog.objects.all()   
    
    if 'logout' in request.GET:
        logout(request)
        
    user_is_login = False    
    if request.user is not None and request.user.is_active:
        user_now = request.user.username      
        user_is_login = True        
        
    if 'yj' in request.GET:
        author = Account.objects.get(Username=user_now)
        blog = Blog.objects.create(Username=author,
                                   Passage=request.GET['yj'],
                                   Tag = request.GET['yj_tag']     )
        return HttpResponseRedirect("../../",locals())                        
    return render_to_response('index.html',locals())
    

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            auth.login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("../../")
        else:
            # Show an error page
            return HttpResponseRedirect("/account/invalid/")
    return render_to_response('login.html',locals())


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("../",locals())

def register_view(request):
    if request.method == 'POST':
        account_form = AccountForm(request.POST,request.FILES)
        if account_form.is_valid():
            new_account = Account()
            new_account.Username = account_form.cleaned_data['Username']
            new_account.Email = account_form.cleaned_data['Email']
            new_account.Image = account_form.cleaned_data['Image']
            new_account.save()
            
            User.objects.create_user(new_account.Username, new_account.Email, account_form.cleaned_data['password'])
            return HttpResponseRedirect("/login/")        
    else:
        account_form = AccountForm()
    return render_to_response('register.html',locals())


       
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
    
def go_out(request):
    if  request.user is not None and request.user.is_active:
        user_now = request.user.username
        if request.method == 'POST':
            plan_form = PlanForm(request.POST)
            if plan_form.is_valid():
                new_plan = Travel_plan()
                
                new_plan.Username = Account.objects.get(Username=user_now)
                new_plan.Destination = plan_form.cleaned_data['Destination']
                new_plan.Start_place = plan_form.cleaned_data['Start_place']
                new_plan.Start_date = plan_form.cleaned_data['Start_date']
                new_plan.End_date = plan_form.cleaned_data['End_date']
                new_plan.People_amount = plan_form.cleaned_data['People_amount']
                new_plan.Budget = plan_form.cleaned_data['Budget']
                new_plan.Demand = plan_form.cleaned_data['Demand']
                new_plan.save()
                return HttpResponse('travel plan post success')
            
        else:
            plan_form = PlanForm()
    
        return render_to_response('go_out.html',locals())
    else:
        return HttpResponse('please login first')
        
            
def diary(request):
    if request.user is not None and request.user.is_active:
        user_now = request.user.username 
        if request.method == 'POST':
            diary_form = DiaryForm(request.POST,request.FILES)
            if diary_form.is_valid():
                    
                    
                    province = request.POST['ddlProvince']
                    city = request.POST['ddlCity']
    
                    new_diary = Diary()
                    new_diary.Username = Account.objects.get(Username=user_now)
                    new_diary.Title = diary_form.cleaned_data['Title']
                    new_diary.Passage = diary_form.cleaned_data['Passage']
                    new_diary.Tag = diary_form.cleaned_data['Tag']
                    new_diary.Image = diary_form.cleaned_data['Image']
                    new_diary.Destination = province+' '+city
                    new_diary.save()        
                    
                    
                    return HttpResponse('diary post success')
        else:
            diary_form = DiaryForm()
    else:
        return HttpResponse('please login first')
    return render_to_response('yj.html',locals())    
    
    
    
    
    
    
    
    
    
    
    
    
    