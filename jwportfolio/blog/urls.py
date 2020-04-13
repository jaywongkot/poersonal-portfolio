from django.urls import path
# Import PostListView for class based view
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView
)
# Import views for function based view
from . import views

urlpatterns = [
    # Use class based view to render blog-homepage
    path('', PostListView.as_view(), name='blog-home'),
    # Here we render a postdetailview with a primary key (int:pk)
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    # This one will actually share a template with the update view that we're going to be creating and
    # they actually expect this template to be the name of the model followed by underscore form (post_form.html)
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    # Use function based view to render blog-homepage
    # path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
]
