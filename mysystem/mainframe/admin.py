from django.contrib import admin
from mainframe.models import User,Computer
# Register your models here.
class User_Admin(admin.ModelAdmin):
    list_display = ('username','password','is_manager','sex','created_at',)
class Computer_Admin(admin.ModelAdmin):
    list_display = ('computername','memory','state','user','created_at',)
admin.site.register(User,User_Admin)
admin.site.register(Computer,Computer_Admin)
