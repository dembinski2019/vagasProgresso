from django import forms
from .models import Employtment

class EmploytmentForm(forms.ModelForm):
    class Meta:
        model = Employtment
        fields = ['employtment_name','slug','requirements',
        'description', 'salary','jobs_vacancy']

