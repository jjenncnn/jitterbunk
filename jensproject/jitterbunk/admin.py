from django.contrib import admin

from .models import User, Bunk, Bunkform

admin.site.register(User)
admin.site.register(Bunk)
admin.site.register(Bunkform)