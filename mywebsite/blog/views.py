from django.shortcuts import render
from .models import ModelPostingan

def blog(request):
    semuaPostingan = ModelPostingan.objects.all();
    context = {
        'title':'Halaman Blog',
        'heading': 'Blog my website',
        'category':'All',
        'BlogPost':semuaPostingan, 
        'nav': [
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/login', 'Login'],
        ]
    }
    return render(request, 'blog/blog.html', context)


def index(request):
    posts = ModelPostingan.objects.all();
    categories = ModelPostingan.objects.values('category').distinct();
    context = {
		'Judul':'Home Blog',
		'Content':'ini adalah halaman blog',
		'Categories':categories,
		'Posts':posts,
    }
    return render(request, 'blog/index.html', context)

def categoryPost(request, categoryInput):
    posts = ModelPostingan.objects.all();
    categories = ModelPostingan.objects.values('category').distinct();
    context = {
		'Judul':'Home Blog',
		'Content':'Tampilkan berdasarkan kategori',
		'Categories':categories,
		'Posts':posts,
    }
    return render(request, 'blog/category.html', context)

def detailPost(request, slugInput):
    posts = ModelPostingan.objects.all();
    categories = ModelPostingan.objects.values('category').distinct();
    context = {
		'Judul':'Home Blog',
		'Content':'Ini halaman blog',
		'Categories':categories,
		'Posts':posts,
    }
    return render(request, 'blog/detail.html', context)
