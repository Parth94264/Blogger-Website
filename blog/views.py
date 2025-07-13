from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Blogger, Blog
from .froms import ContactForm,BlogForm
from django.core.mail import send_mail
from django.http import HttpResponse



@login_required(login_url="/login")
def home(request):
    blogger = get_object_or_404(Blogger, user=request.user)
    blogs = Blog.objects.all()
    blog_count = Blog.objects.filter(author=blogger).count()
    
    if request.GET.get('search'):
        print(request.GET.get('search'))
        blogs = blogs.filter(title__icontains=request.GET.get('search'))
        
    context = {"blogger": blogger, "blogs_count": blog_count, "blogs": blogs}
    return render(request, 'blog/index.html', context)

@login_required(login_url="/login")
def my_profile(request):
    blogger = get_object_or_404(Blogger, user=request.user)
    blogs = Blog.objects.filter(author=blogger)
    blog_count = Blog.objects.filter(author=blogger).count()
    
    if request.GET.get('search'):
        print(request.GET.get('search'))
        blogs = blogs.filter(title__icontains=request.GET.get('search'))
        
    context = {"blogger": blogger, "blogs_count": blog_count, "blogs": blogs}
    return render(request, 'blog/myprofile.html', context)

@login_required(login_url="/login")


def create_blog(request):
    if request.method == 'POST':
       
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
          
            new_blog = form.save(commit=False)
            new_blog.author = request.user.blogger 
            new_blog.save()
            
            return redirect('/myprofile')  
    else:
       
        form = BlogForm()

    return render(request, "blog/create_blog.html", {'form': form})


@login_required(login_url="/login")
def delete_blog(request, id):
    queryset = Blog.objects.filter(id=id)
    queryset.delete()
    return redirect('/myprofile')

@login_required(login_url="/login")
def all_detailed_blog(request, id):
    blog = get_object_or_404(Blog, pk=id)

    
    print(request.user in blog.viewers.all())
    if request.user not in blog.viewers.all():
        blog.views += 1
        blog.viewers.add(request.user)
        blog.save()
        
    if request.method == "POST":
        rating = request.POST.get('rating')
        if blog.views == 1:
            blog = Blog.objects.get(id=id)
            blog.rating = float(rating)
            blog.save() 
        else:
            blog = Blog.objects.get(id=id)
            final = (blog.rating + float(rating)) / 2
            blog.rating = final
            blog.save()
            
        context = {'blog': blog}
        return render(request, "blog/all_detailed_blog.html", context)
        
    context = {'blog': blog}
    return render(request, "blog/all_detailed_blog.html", context)

@login_required(login_url="/login")
def my_detailed_blog(request, id):
    blog = Blog.objects.get(id=id)
    context = {'blog': blog}
    return render(request, "blog/my_detailed_blog.html", context)

@login_required(login_url="/login")
def update_blog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog.title = title
        blog.content = content
        blog.save()
        context = {'blog': blog}
        return render(request, "blog/my_detailed_blog.html", context)
    context = {'blog': blog}
    return render(request, "blog/update_blog.html", context)

@login_required(login_url="/login")
def other_blogger(request, id, blog_id):
    blog = Blog.objects.get(id=blog_id)
    blogger = get_object_or_404(Blogger, user=blog.author.user)
    blogs = Blog.objects.filter(author=blogger)
    blog_count = Blog.objects.filter(author=blogger).count()
    
    user = User.objects.get(pk=id)
    
    context = {"user": user, "blog": blog, "blog_count": blog_count, "blogs": blogs}
    return render(request, "blog/other_blogger.html", context)

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Render the same template with a success message
            return render(request, 'blog/contact.html', {'form': ContactForm(), 'success': True})
    else:
        form = ContactForm()

    return render(request, 'blog/contact.html', {'form': form})
