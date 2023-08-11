from django.shortcuts import render
from .models import Post #models is in same directory that is why we are using .models

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # here the third argument is that we are passing 
    # something in title like in this case it would be Django Blog - About and if we do not pass anyting then it
    # will take the else condition which is Django Blog