"""jwportfolio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
# To upload a a media and static file, you have to import settings and static
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),

    path('blog/', include('blog.urls')),
    path('blog/register/', user_views.register, name='register'),
    path('blog/profile/', user_views.profile, name='profile'),
    # This a class base view
    path('blog/login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('blog/logout/', auth_views.LogoutView.as_view(
        template_name='users/logout.html'), name='logout'),
]

# Add media and static files for the debug mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
