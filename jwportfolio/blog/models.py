from django.db import models
from django.utils import timezone
# Import user model from Django library
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    # [1] models.DateTimeField(auto_now=true), to update a blog post base on a current user login timzone which is not consistency
    #     for our blog post if we have million useres from over different timezone. This would be great for a last modified field.
    # [2] models.DateTimeField(auto_now_add=true)  This would set the date posted to the current date time only when this object is created.
    #     But with the auto_now_add=true, you can't ever update the value of the date posted so it will have to keep the exact date time
    #     of when the post was created.
    # [3] models.DateTimeField(default=timezone.now) This option will do the same with option no.2 but you have the option of changing the date.
    #     We don't put a parentheses after default=timzone.now eventhrough it is a function because we don't want it to excute.
    #     We just a default value of this function.
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
