from django.shortcuts import render

def index(request):
    context = {
        'title':'Halaman Utama',
        'nav':[
            ['/', 'Home'],
            ['/blog', 'Blog'],
            ['/login', 'Login'],
            ['/admin', 'Admin'],
        ]
    }
    return render(request, 'index.html', context)