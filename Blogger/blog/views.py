from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import *
from django.shortcuts import get_object_or_404


@login_required(login_url="/login")
def home(request):
    
    blogger = get_object_or_404(Blogger, user=request.user)
    blogs = Blog.objects.all()
    blog_count = Blog.objects.filter(author=blogger).count()
    
    if request.GET.get('search'):
        print(request.GET.get('search'))
        blogs= blogs.filter(title__icontains = request.GET.get('search'))
        
    
    context = {"blogger": blogger, "blogs_count":blog_count, "blogs" : blogs}
    return render (request, 'blog/index.html', context)

def my_profile(request):
    blogger = Blogger.objects.filter(user=request.user)
    blogger = get_object_or_404(Blogger, user=request.user)
    blogs = Blog.objects.filter(author=blogger)
    blog_count = Blog.objects.filter(author=blogger).count()
    
    
    if request.GET.get('search'):
        print(request.GET.get('search'))
        blogs= blogs.filter(title__icontains = request.GET.get('search'))
        
        
    context = {"blogger": blogger, "blogs_count":blog_count, "blogs" : blogs}
    return render(request, 'blog/myprofile.html', context)


def create_blog(request):
    
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        author = request.user.blogger  # Assuming you have a one-to-one relationship between User and Blogger

        new_blog = Blog(title=title, content=content, author=author)
        new_blog.save()

        return redirect('/myprofile')
        
        
    return render(request, "blog/create_blog.html")


def delete_blog(request, id):
    queryset = Blog.objects.filter(id = id)
    queryset.delete()
    return redirect('/myprofile')

def all_detailed_blog(request, id):
 
    blog = get_object_or_404(Blog, pk=id)

    # Check if the user has already viewed the blog
    print(request.user in blog.viewers.all())
    if request.user not in blog.viewers.all():
        # final = (blog.rating + float(0))/2
        # blog.rating = final
        blog.views += 1
        blog.viewers.add(request.user)
        blog.save()
        
    if request.method == "POST":
        rating = request.POST.get('rating')
        if blog.views == 1:
            blog = Blog.objects.get(id=id)
            blog.rating = float(rating)
            blog.save() 
        else :
            blog = Blog.objects.get(id=id)
            final = (blog.rating + float(rating))/2
            blog.rating = final
            # blog.save() 
        context = {'blog':blog}
        return render(request, "blog/all_detailed_blog.html", context)
        
    # blog.save()
    context = {'blog':blog}
    return render(request, "blog/all_detailed_blog.html", context)

def my_detailed_blog(request, id):
    blog = Blog.objects.get(id = id)
    context = {'blog':blog}
    return render(request, "blog/my_detailed_blog.html", context)

def update_blog(request, id):
    blog = Blog.objects.get(id = id)
    if request.method == "POST":
        title = request.POST.get('title')
        content = request.POST.get('content')
        blog.title = title
        blog.content = content
        blog.save()
        context = {'blog':blog}
        return render(request, "blog/my_detailed_blog.html", context)
    context = {'blog':blog}
    return render(request, "blog/update_blog.html", context)


def other_blogger(request, id, blog_id):
    blog = Blog.objects.get(id = blog_id)
    blogger = get_object_or_404(Blogger, user = blog.author.user)
    blogs = Blog.objects.filter(author=blogger)
    blog_count = Blog.objects.filter(author=blogger).count()
    
    user = User.objects.get(pk = id)
    
    context = {"user": user, "blog":blog, "blog_count":blog_count, "blogs":blogs}
    return render(request, "blog/other_blogger.html", context)