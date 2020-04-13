from django.shortcuts import render
# Here we import ListView and DetailView which is a class based view
from django.views.generic import (
    ListView,
    DetailView,
    CreateView
)
# From a models.py in the same directory, we import a Post class
from .models import Post
# Import HttpResponse only need when we want to return http resquest function
# from django.http import HttpResponse

# We created dummy posts to render in home view and to loop through in home.html template
# posts = [
#     {
#         'author': 'JayWongkot',
#         'title': 'Blog Post 1',
#         'content': 'First post content',
#         'date_posted': 'April 05, 2020'
#     },
#     {
#         'author': 'Oppa Aui',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 06, 2020'
#     }
# ]


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

# Create a class based view and use a ListView to render our post list


class PostListView(ListView):
    model = Post
    # We hav to change a location of template where will look to render on homepage from blog/post_list.html to blog/home.html
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    # By default, django will list our post base on a list variable
    # but in our case we have set our post list variable to posts as in context
    context_object_name = 'posts'
    # Reorder post from the latest post to oldest post
    ordering = ['-date_posted']


class PostDetailView(DetailView):  # We create a PostDetailView for each post
    model = Post  # Render a template as default which is post_detail.html


class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    # Overide a form valid mehtod to allow the author to create a new post
    # that will allow us to add the author before the form submit
    def form_valid(self, form):
        # Basically this is saying hey that forum that you are trying to submit before you do that
        # take that instance and set the author equal to the current logged end user
        form.instance.author = self.request.user
        # Then we can validate the form
        return super().form_valid(form)


def about(request):
    # return HttpResponse('<h1>Blog About</h1>')
    # If a dictionary is very short, we don't need to declare it. We can passe it into render directly as below
    return render(request, 'blog/about.html', {'title': 'About'})
