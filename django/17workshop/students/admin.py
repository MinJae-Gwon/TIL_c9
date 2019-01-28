from django.contrib import admin
from .models import Students
# Register your models here.

# class StudentAdmin(admin.ModelAdmin):
#     list_display = ('name','email','birthday','age',)
# admin.site.register(Students, StudentAdmin)
admin.site.register(Students)
