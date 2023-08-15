# Each URL pattern is associated with a specific view that should be executed when a request matches that pattern.
# When a user enters a URL in their browser, the Django server receives the request and looks at the urls.py file to determine which view should handle the request.
from django.urls import path
from .views import (
    PostListView,
    PostDetailView, 
    PostCreateView,
)
from .import views

urlpatterns = [
    # path('', views.home, name='blog-home'), # not using this as now we will be ising the class based views which will give us more functionality 
    path('', PostListView.as_view(), name='blog-home'), # we cannot pass PostListView directly so we need as view method to pass it
    
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'), # post/<int>pk> grabs the value from the URL and use it into our views function 
    # as in this case we are using class based views so that will be passed to a class based views, int over there means that we 
    # want out primary key to be an integer

    path('post/new/', PostCreateView.as_view(), name='post-create'),

    path('about/', views.about, name='blog-about'),
]

