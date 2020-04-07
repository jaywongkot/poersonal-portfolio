from django.shortcuts import render
# From a models.py in the same directory, we import a Post class
from .models import Post
# from django.http import HttpResponse # Import HttpResponse only need when we want to return http resquest function

# We created dummy posts to render in home view and to loop through in home.html template
posts = [
    {
        'author': 'JayWongkot',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 05, 2020'
    },
    {
        'author': 'Oppa Aui',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 06, 2020'
    }
]


def home(request):
    # we created a dictionary to pass a data that we pretended to call and response from a database
    # context = {
    #     'posts': posts  # We created a key and passed in a dictionary that we created at the top
    # }

    context = {
        # We will fetch a data from a database instead of a dummy posts
        'posts': Post.objects.all()
    }
    # return HttpResponse('<h1>Blog Home</h1>')
    # We passed in a third argument as 'context' to render a dummy post
    return render(request, 'blog/home.html', context)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    # If a dictionary is very short, we don't need to declare it. We can passe it into render directly as below
    return render(request, 'blog/about.html', {'title': 'About'})
