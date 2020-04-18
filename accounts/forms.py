from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from .models import User, Candidate, Company

class CandidateSignUpForm(UserCreationForm):
    
    class Meta(UserCreationForm.Meta):
        model = User
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_candidate = True
        user.save()
        candidate = Candidate.objects.create(user=user)
        return user



class CompanySignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User


    @transaction.atomic
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_company = True
        if commit:
            user.save()
            company = Company.objects.create(user=user)
        return user


class EditCandidateForm(forms.ModelForm):

    class Meta:
        
        model = Candidate
        fields = ['cpf', 'whatsapp', 'curriculum']

class EditCompanyForm(forms.ModelForm):

    class Meta:
        model = Company
        fields = ['cnpj', 'whatsapp', 'responsibly']


class EditAccountForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name']

    