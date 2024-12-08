
from django.contrib.auth import authenticate , login, logout
from django.shortcuts import render, redirect
from mooseapp.models import Post , Comment , Contact , Category
from .pagenations import Pagination
# Create your views here.

def home(request):
    posts = Post.objects.all()
    a = {
        'posts': posts
    }
    return render(request, 'index.html', context=a)


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        subject = data.get('subject')

        obj = Contact.objects.create( name = name, email = email, subject = subject)
        obj.save()
        return redirect('/contact')

    return render(request, 'contact.html')


def blog(request):
    posts = Post.objects.all().order_by('-created_at')
    pagenator = Pagination(posts , 1)
    data = request.GET
    page = int(data.get('page' , 1 ))
    b = {
        'posts': pagenator.get_page(page),
        'page_count': range( 1 , pagenator.page_count + 1),
        'current_page': page,
        'next_page' : page + 1,
        'prev_page': page - 1,
        'is_last' : pagenator.is_last(page),
        'is_first' : pagenator.is_first(page)
    }
    return render(request, 'blog.html' ,context=b)








def blog_single(request, pk):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        print(name)
        email = data.get('email')
        print(email)
        message = data.get('message')
        print(message)
        website = data.get('website')
        print(website)

        post = Post.objects.get(id=pk)
        obj = Comment.objects.create(name=name, email=email, message=message, website=website, post=post)
        obj.save()

    post = Post.objects.get(id=pk)
    comments = Comment.objects.filter(post=post)
    a = {
        'post': post,
        'comments': comments
    }

    return render(request, 'blog-single.html', context=a)




def category(request , pk):
    posts = Post.objects.filter(category__name=pk)
    pagenator = Pagination(posts , 1)
    data = request.GET
    page = int(data.get('page' , 1 ))
    b = {
        'posts': pagenator.get_page(page),
        'page_count': range( 1 , pagenator.page_count + 1),
        'current_page': page,
        'next_page' : page + 1,
        'prev_page': page - 1,
        'is_last' : pagenator.is_last(page),
        'is_first' : pagenator.is_first(page)
    }
    # a = {
    #     'posts':posts,
    #     # 'post':post
    # }
    return render(request , 'category.html' , context=b )







def login_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        # user = User.objects.filter(username=username).first()
        auth = authenticate(request , username=username , password=password)

        if auth:
            login(request , auth)
        # if not user:
        return render( request , 'login.html' , context={'error': 'username or password  incorrect'})




    return render(request, 'login.html')



def logout_view(request):
    logout(request)
    return redirect('/')







def register_view(request):
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
    return render(request , 'register.html')






















