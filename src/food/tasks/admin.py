from django.contrib import admin
from tasks.models import Spotlight



class SpotlightAdmin(admin.ModelAdmin):
    list_display = ["name","food_image","fod_name","price"]
    
admin.site.register(Spotlight,SpotlightAdmin)