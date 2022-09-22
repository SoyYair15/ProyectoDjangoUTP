from django.contrib import admin
from . models import (
    BLOG,
    REVIEW,
)

@admin.register(BLOG)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)

@admin.register(REVIEW)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'is_active')
    readonly_fields = ('slug',)
    
#DEFINE LO QUE TE SALDRA EN EL APARTADO DEL ADMINISTRADOR