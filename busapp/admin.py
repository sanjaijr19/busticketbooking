from django.contrib import admin
from busapp.models import Driver,User
class DriverAdmin(admin.ModelAdmin):
    driverdetails=["drivername","age","contact_no","bus_no"]

class UserAdmin(admin.ModelAdmin):
    userdetails=["user_id","email","name","password"]

admin.site.register(Driver,DriverAdmin)
admin.site.register(User,UserAdmin)

# Register your models here.
