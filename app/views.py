from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from app.forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from app.models import *
#from django.contrib.auth import login as auth_login

# Create your views here.
@login_required(login_url='login')
def dashboard(request):
    hood = Hood.objects.all()
    context={
        'hood':hood,
    }
    return render(request, 'hoods.html',context)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


@login_required(login_url='login')
def profile(request, username):
    if request.method == 'POST':
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if prof_form.is_valid():
            prof_form.save()
            return redirect(request.path_info)
    else:
        prof_form = UpdateUserProfileForm(instance=request.user.profile)

    context = {
        'prof_form': prof_form,
         }
    return render(request, 'profile.html', context)

def join_hood(request, id):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = hood
    request.user.profile.save()
    return redirect('dashboard')


def leave_hood(request, id):
    hood = get_object_or_404(Hood, id=id)
    request.user.profile.hood = None
    request.user.profile.save()
    return redirect('dashboard')

def hood(request, id):
    hood = Hood.objects.get(id=id)
    members = Profile.objects.filter(hood=hood)
    business = Business.objects.filter(hood=hood)
    posts = Post.objects.filter(hood=hood)
    
    context = {
        'hood': hood,
        'business': business,
        'posts': posts,
        'members':members,
    }
    return render(request, 'myhood.html', context)

def post(request, id):
    hood = Hood.objects.get(id=id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.hood = hood
            post.user = request.user.profile
            post.save()
            return redirect('hood', hood.id)
    else:
        form = PostForm()
    return render(request, 'post.html', {'form': form})


def business(request, id):
    hood = Hood.objects.get(id=id)
    if request.method == 'POST':
        form = BusinessForm(request.POST)
        if form.is_valid():
            b_form = form.save(commit=False)
            b_form.hood = hood
            b_form.user = request.user.profile
            b_form.save()
            return redirect('hood', hood.id)
    else:
        form = BusinessForm()
    return render(request, 'business.html', {'form': form})


def search_business(request):
    if request.method == 'GET':
        name = request.GET.get("title")
        results = Business.objects.filter(name__icontains=name).all()
        print(results)
        message = f'name'
        context = {
            'results': results,
            'message': message
        }
        return render(request, 'results.html', context)
    else:
        message = "You haven't searched for any image category"
    return render(request, "results.html")
    



