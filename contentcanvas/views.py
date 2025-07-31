from django.shortcuts import render,HttpResponse,get_object_or_404
from blog.models import Category,Blog

def home(request):
    categories=Category.objects.all()
    blog=Blog.objects.all().filter(trending=True,status='Published').order_by('-created_at')
    pposts=Blog.objects.all().filter(trending=False,status='Published').order_by('-created_at')
    context={
        'categories':categories,
        'blog':blog,
        'pposts':pposts
    }
    return render(request,'home.html',context)

def posts_by_category(request,cname):
    categories=Category.objects.all()
    category=Category.objects.get(cname=cname)
    blogs=Blog.objects.all().filter(category=category.id)
    context={
        'categories':categories,
        'blogs':blogs
    }

    return render(request,'posts_by_category.html',context)

def single_blog(request,slug):
    categories=Category.objects.all()
    blog=get_object_or_404(Blog,slug=slug,status='Published')
    context={
        'categories':categories,
        'blog':blog
    }
    return render(request,'single_blog.html',context)