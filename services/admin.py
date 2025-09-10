
from django.contrib import admin
from .models import Service, Review

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title','seller','price','category','delivery_time','created_at')
    list_filter = ('category','created_at')
    search_fields = ('title','description','seller__username')

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('service','buyer','rating','created_at')
    list_filter = ('rating','created_at')
