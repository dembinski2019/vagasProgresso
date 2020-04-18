from django.contrib import admin
from .models import Employtment, Apply_for

class EmploytmentAdmin(admin.ModelAdmin):
    list_display = ['company','employtment_name','jobs_vacancy','salary','created_at']
    search_fields = ['employtment_name',]



admin.site.register(Employtment,EmploytmentAdmin)
admin.site.register(Apply_for)

