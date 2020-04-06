from django.contrib import admin

from .views import *

admin.site.register(About)  # About model from model.py file
admin.site.register(Service)  # Service model from model.py file
admin.site.register(RecentWork)  # RecentWork model from model.py file
admin.site.register(Client)  # Client model from model.py file
