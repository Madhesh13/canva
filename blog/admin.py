from django.contrib import admin
from blog.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display=['cname','created_at','updated_at']

admin.site.register(Category,CategoryAdmin)