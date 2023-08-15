from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User 
from django.urls import reverse
# we want to make sure that there should be single user for many posts this is one to many relationship to do this
# in django we use foreign key

class Post(models.Model):
    title = models.CharField(max_length=100) # this is for title as a title can have max Length 100
    content = models.TextField() # A text field can have any field the reason we have used text field here because we want it in paragraph there will be many lines
    date_posted = models.DateTimeField(default = timezone.now) # we can have different formats like when the user createed the post we want the post time instant but we cannot modify that one, to modify we are using this using import
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # if the user who created the post get deleted the we want all his posts also to be deleted

    def __str__(self): # watch oops series for this dunder str method
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk}) # returning the full path as a string



