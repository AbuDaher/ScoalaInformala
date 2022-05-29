from django.shortcuts import render, redirect
from .forms import RegisterForm, PostForm
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,logout, authenticate
from .models import Post
from django.contrib.auth.models import User, Group


@login_required(login_url='/login')
def home(request):
    posts = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("aplicatie1.delete_post")):
                post.delete()
        elif user_id:
            user= User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.filter(name="default")
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.filter(name="mod")
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'aplicatie1/home.html', {"posts" : posts})


@login_required(login_url='/login')
def actuals(request):
    posts1 = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("aplicatie1.delete_post")):
                post.delete()
        elif user_id:
            user= User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.filter(name="default")
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.filter(name="mod")
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'aplicatie1/actuals.html', {"posts1" : posts1})


def planning(request):
    posts2 = Post.objects.all()

    if request.method == "POST":
        post_id = request.POST.get("post-id")
        user_id = request.POST.get("user-id")

        if post_id:
            post = Post.objects.filter(id=post_id).first()
            if post and (post.author == request.user or request.user.has_perm("aplicatie1.delete_post")):
                post.delete()
        elif user_id:
            user= User.objects.filter(id=user_id).first()
            if user and request.user.is_staff:
                try:
                    group = Group.objects.filter(name="default")
                    group.user_set.remove(user)
                except:
                    pass
                try:
                    group = Group.objects.filter(name="mod")
                    group.user_set.remove(user)
                except:
                    pass

    return render(request, 'aplicatie1/planning.html', {"posts2" : posts2})


@login_required(login_url="/login")
@permission_required("aplicatie1.add_post", login_url="/login", raise_exception=True)


def create_post_actuals(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/actuals")
    else:
        form = PostForm()

    return render(request, 'aplicatie1/create_post_actuals.html', {"form": form})

def create_post_planning(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect("/planning")
    else:
        form = PostForm()

    return render(request, 'aplicatie1/create_post_planning.html', {"form": form})



def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('/home')
    else:
        form = RegisterForm()
    return render(request,'registration/sign_up.html', {"form": form})