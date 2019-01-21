from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.core.paginator import Paginator, EmptyPage,PageNotAnInteger
from .forms import RegisterForm
from django.contrib import messages
from .models import Post

# Create your views here.
def IndexView(request):
    post = Post.objects.all()

    paginator = Paginator(post, 12) # Show 25 contacts per page
    page = request.GET.get('page')
    total_article = paginator.get_page(page)

    return render(request, 'index.html',{'post':total_article})

def getSingle(request, id):
    single_post = get_object_or_404(Post, pk=id)
    first_slide = Post.objects.first()
    last_slide = Post.objects.last()

    return render(request, 'single.html',{'sp':single_post, 'f':first_slide, 'l':last_slide})

def loginSys(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method == 'POST':
            user = request.POST.get('username')
            pas = request.POST.get('pass')

            auth = authenticate(request, username=user, password=pas)

            if auth is not None:
                login(request, auth)
                return redirect('index')
                messages.SUCCESS(request, 'You have successfully Login')
            else:
                messages.add_message(request, messages.ERROR, 'Username and Password mismatch.')

    return render(request, 'login.html')

def getLogout(request):
    logout(request)
    return redirect('login')

def registerUser(request):
    form = RegisterForm

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('login')
    return render(request, 'register.html',{'form':form})

def category(request):
    return render(request, 'category.html')

def profileAuth(request):
    return render(request, 'profile.html')


