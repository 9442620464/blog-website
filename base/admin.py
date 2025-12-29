from django.contrib import admin
from base.models import Category,Articles
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display=['category_name']

class ArticlesAdmin(admin.ModelAdmin):
    list_display=['title','author','Category','created_on','status']
    prepopulated_fields={
        'slug':['title']
    }


admin.site.register(Category,CategoryAdmin)
admin.site.register(Articles,ArticlesAdmin)