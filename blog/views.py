# views takes http request and return http response
# Views often use models to retrieve data from the database, process it, and pass it to templates for rendering.

# Here are the key characteristics and advantages of class-based views:
# Object-Oriented Approach: Class-based views use object-oriented programming concepts to define views as classes.
# Each class-based view is an instance of a class that inherits from one of Django's class-based view mixins.

# Reusability and Composition: Class-based views encourage code reusability by allowing you to create view classes that can be easily extended or customized.
# You can inherit from existing class-based views and override or add specific methods to modify their behavior.

# Generic Views: Django's generic class-based views are pre-built views that cover common use cases, such as displaying lists of objects, detail views, and form handling.
# You can use these generic views as a foundation and customize their behavior to fit your needs.


# -> We aur using class based views bczz it has lot of functionality and can handle a lot of backend easily it has
# like create views update views delete views and a lot more functionality


from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from .models import Post #models is in same directory that is why we are using .models

def home(request):
    context = {
        'posts': Post.objects.all(),
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post # The model class you provide to the ListView defines the type of objects you want to display.
    template_name = 'blog/home.html' #by default it was loking at some another location so changing the location # <app>/<model>_<viewtype>/html
    context_object_name = 'posts' # on posts it will be looping through we have already created this in context
    ordering = ['-date_posted'] # orders post from newest to oldest

class PostDetailView(DetailView): # This is for the details of the already created post
    model = Post

class PostCreateView(LoginRequiredMixin ,CreateView): # This is for creating  a new post
    # using loginrequired mixin so that it checks everytime that a user is logged in, it will automatically redirect to login page if the user is not logged in
    model = Post
    fields = ['title', 'content']

    # IntegrityError at /post/new/
    # NOT NULL constraint failed: blog_post.author_id
    # To remove this error we have to set author, got this error while trying to post the blog post

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # ImproperlyConfigured at /post/new/
    # No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
    # Now you will be getting this error message for this we have to redirect the route and we can use the reverse function
    # the reason we will be using reverse function not redirect bczz it reverse a string to that route instead of redirecting it.
    
    

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'}) # here the third argument is that we are passing 
    # something in title like in this case it would be Django Blog - About and if we do not pass anyting then it
    # will take the else condition which is Django Blog


