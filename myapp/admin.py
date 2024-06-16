from django.contrib import admin

# Register your models here.
from  .models import Category ,Post
admin.site.register(Category)
admin.site.register(Post)

class Post(admin.ModelAdmin):
    fields=["title,category,job_title,description,image,content_type"]
