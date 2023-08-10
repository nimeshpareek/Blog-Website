from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'Nimesh',
        'title': 'Atomic Python',
        'content': 'self-help',
        'date_posted': '09-08-2023'
    },
    {
        'author': 'Sudhir',
        'title': 'Time Waste',
        'content': 'Waste',
        'date_posted': '08-08-2023'
    },
]

def home(request):
    # we can pass the above data to the dictionary and above dictionary name is context
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # here the third argument is that we are passing 
    # something in title like in this case it would be Django Blog - About and if we do not pass anyting then it
    # will take the else condition which is Django Blog