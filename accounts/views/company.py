from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from ..models import User
from ..forms import CompanySignUpForm


class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'accounts/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'company'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('conta_profile')
        