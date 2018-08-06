from django.contrib import admin
from .models import UserInfo
# Register your models here.

@admin.register(UserInfo)
class Userinfo_admin(admin.ModelAdmin):
    list_display = ["uname", "uemail", "urecive",
                    "uaddress", "upost", "uphone"]

    list_per_page = 15
