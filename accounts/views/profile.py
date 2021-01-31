from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView
from django.contrib.auth.decorators import login_required
from ..forms import EditAccountForm, EditCandidateForm,EditCompanyForm
from ..models import Candidate,Company
from core.models import Employtment,Apply_for
from ..decorators import company_required, candidate_required
from django.contrib.auth.mixins import LoginRequiredMixin


class ProfileTemplateView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    

@login_required
def edit_profile_candidate(request):
    context = {}
    template_name = 'accounts/edit_profile.html'
    user = request.user
    formUser = EditAccountForm(request.POST or None,instance=user)
    candidate = Candidate.objects.get(user_id=user.id)

    if request.method == 'POST':
        userForm = EditCandidateForm(request.POST, request.FILES, instance=candidate)
        if formUser.is_valid() and userForm.is_valid():
            formUser.save()
            userForm.save()
            context['sucess'] = True
    else:
        userForm = EditCandidateForm(instance=candidate)

    context['formUser'] = formUser
    context['userForm'] = userForm

    return render(request, template_name, context)

@login_required
def edit_profile_company(request):
    context = {}
    template_name = 'accounts/edit_profile.html'
    user = request.user
    compamy = Company.objects.get(user_id=user.id)
    userForm = EditCompanyForm(request.POST or None, instance=compamy)
    formUser = EditAccountForm(request.POST or None,instance=user)
    if request.method == 'POST':
        if formUser.is_valid() and userForm.is_valid():
            formUser.save()
            userForm.save()
            context['sucess'] = True
    context['formUser'] = formUser
    context['userForm'] = userForm
    return render(request, template_name, context)



@login_required
@company_required
def my_employtment(request):
    context={}
    user = request.user
    employtmente = Employtment.objects.filter(company_id=user)
    if employtmente:
        context['sucess'] = True
        context['employtment']=employtmente
    template_name = 'accounts/list_employtment.html'
    return render(request,template_name, context)

@login_required
def my_profile(request):
    context = {}
    template_name = 'accounts/list_profile.html'
    user = request.user
    
    if user.is_candidate:
        candidate = Candidate.objects.get(user_id=user.id)
        context['dataUser'] = candidate

    elif user.is_company:
        compamy = Company.objects.get(user_id=user.id)        
        context['dataUser'] = compamy

    return render(request, template_name, context)

@login_required
@company_required
def candidate_apply_for_amploytment(request,id):
    context = {}
    job = Employtment.objects.get(id=id)
    enrollment = Apply_for.objects.filter(job_id=id)
    if enrollment:
        context['sucess'] = True
    context['job']=job
    context['enrollment'] = enrollment
    template_name = 'accounts/candidate_apply_for_amploytment.html'
    return render(request,template_name,context )
    
@login_required
@candidate_required
def candidate_enrollment(request):
    context = {}
    user = request.user.id
    enrollment = Apply_for.objects.filter(candidate_id=user)
    if enrollment:
        context['sucess'] = True
        context['enrollment'] = enrollment
    template_name = 'accounts/list_enrollment.html'
    return render(request,template_name, context)


def candidate_enrollment_download_curriculum(request, id):
    pass    