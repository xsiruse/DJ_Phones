from django.contrib import admin
from phones.models import Phone


# Register your models here.
class PhoneAdmin(admin.ModelAdmin):
    pass


admin.site.register(Phone, PhoneAdmin)
