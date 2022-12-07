from django.contrib import admin

# Register your models here.
from .models import Country

class CustomCountryAdmin(admin.ModelAdmin):
    model = Country
    list_display=('name','desc','author')
    list_filter=('name','desc')
    
    search_fields=('name','desc')
    fieldsets=(('Owner',{'fields':('author',)}),('country info',{'fields':('name','desc',)}),)

admin.site.register(Country,CustomCountryAdmin)