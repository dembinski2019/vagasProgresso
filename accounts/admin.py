from django.contrib import admin
from .models import User,  Candidate

class UserAdmin(admin.ModelAdmin):
    list_display = ['username','first_name','email','is_candidate', 'is_company','is_superuser']
    search_fields = ['username', 'email']


class CandidateAdmin(admin.ModelAdmin):
    list_display = ['curriculum']

admin.site.register(User, UserAdmin)
admin.site.register(Candidate, CandidateAdmin)

# Register your models here.
