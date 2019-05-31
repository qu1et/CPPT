from django.contrib import admin

from .models import Articles

# Register your models here.


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'get_excerpt', 'created_date')


admin.site.register(Articles, ArticleAdmin)
