from django.shortcuts import render,HttpResponse
from blog.models import Category,Blog

def home(request):
    categories=Category.objects.all()
    blog=Blog.objects.all().filter(trending=True).order_by('-created_at')
    context={
        'categories':categories,
        'blog':blog
    }
    return render(request,'home.html',context)


