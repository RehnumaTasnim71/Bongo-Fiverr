
from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','service','buyer','seller','status','created_at')
    list_filter = ('status','created_at')
    search_fields = ('service__title','buyer__username','seller__username')
