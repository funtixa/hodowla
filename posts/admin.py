from django.contrib import admin

from .models import Author, Category, Post, Comment, PostView

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','timestamp','content','post')
    fieldsets = (
        (None, {
            "fields": (
                'user',
                'timestamp',
                'content',
                'post'
            ),
        }),
    )
    

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment, CommentAdmin)
admin.site.register(PostView)

