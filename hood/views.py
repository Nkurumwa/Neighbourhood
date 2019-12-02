from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, AddHoodForm, AddBusinessForm, AddPostForm
from .models import Business, Profile, Join, Neighbourhood, Post
from django.contrib.auth.models import User

def index(request):
    title = 'Home'
    return render(request, 'index.html', {'title':title})

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created successfully')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'registration/register.html', {'form':form})

@login_required
def create_profile(request):
    current_user = request.user
    if request.method=="POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return redirect('/')

    else:

        form = ProfileForm()
    return render(request,'user/profile_form.html',{"form":form})

@login_required
def home(request):
    if request.user.is_authenticated:
        if Join.objects.filter(user_id=request.user).exists():
            hood = Neighbourhood.objects.get(pk=request.user.join.hood_id.id)
            posts = Post.objects.filter(post_hood=request.user.join.hood_id.id)
            businesses = Business.objects.filter(business_hood=request.user.join.hood_id.id)
            return render(request, 'hood/current_hood.html', {"hood": hood, "businesses": businesses, "posts": posts})
        else:
            hoods = Neighbourhood.all_neighbourhoods()
            return render(request, 'hood/home.html', {"hoods": hoods})
    else:
        hoods = Neighbourhood.all_neighbourhoods()
    return render(request, 'hood/home.html', {"hoods": hoods})


@login_required
def add_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.user_profile = current_user
            hood.save()
        return redirect('home')

    else:
        form = AddHoodForm()
    return render(request, 'hood/add_hood.html', {"form": form})

@login_required
def join_hood(request, hood_id):
    neighbourhood = Neighbourhood.objects.get(pk=hood_id)
    if Join.objects.filter(user_id=request.user).exists():
        Join.objects.filter(user_id=request.user).update(hood_id=neighbourhood)
    else:

        Join(user_id=request.user, hood_id=neighbourhood).save()

    return redirect('home')

@login_required
def add_business(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddBusinessForm(request.POST, request.FILES)
        if form.is_valid():
            business = form.save(commit=False)
            business.business_owner = current_user
            business.business_hood = request.user.join.hood_id
            business.save()
        return redirect('home')

    else:
        form = AddBusinessForm()
    return render(request, 'user/add_business.html', {"form": form})


@login_required
def leave_hood(request, hood_id):
    if Join.objects.filter(user_id=request.user).exists():
        Join.objects.get(user_id=request.user).delete()
        return redirect('home')


@login_required
def add_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.poster = current_user
            post.post_hood = request.user.join.hood_id
            post.save()
        return redirect('home')

    else:
        form = AddPostForm()
    return render(request, 'user/add_post.html', {"form": form})


@login_required
def user_profile(request, username):
    profile = User.objects.get(username=username)
    try:
        profile_info = Profile.get_profile(profile.id)
    except:
        profile_info = Profile.filter_by_id(profile.id)
    businesses = Business.get_profile_businesses(profile.id)
    title = f'@{profile.username}'
    return render(request, 'user/profile.html', {'title': title, 'profile': profile, 'profile_info': profile_info, 'businesses': businesses})



def search_results(request):
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        business_results = Business.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message": message, "businesses": business_results})

    else:
        message = "Please enter a search term"
    return render(request, 'search.html', {"message": message})