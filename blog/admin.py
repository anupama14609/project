from django.contrib import admin
from .models import Contact, Post, BlogComment
from django_summernote.admin import SummernoteModelAdmin

class PostAdmin(SummernoteModelAdmin):
     list_display = ('title','content',)
     search_fields = ('title','')
     list_per_page = 10
     summernote_fields = ('content',)



# Register your models here.
admin.site.register(Contact)
admin.site.register(Post, PostAdmin)
admin.site.register(BlogComment)