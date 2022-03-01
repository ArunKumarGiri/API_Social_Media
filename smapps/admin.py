from django.contrib import admin
from .models import Post,Profile,Comments,Like,Friends

# Register your models here.

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Comments)
admin.site.register(Like)
admin.site.register(Friends)