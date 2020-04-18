from django.shortcuts import render, redirect, get_object_or_404
from .models import Employtment, Apply_for
from .forms import EmploytmentForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import candidate_required, company_required
from accounts.models import Candidate

def search(request):
    context = {}
    query = request.GET.get('search')
    jobs = Employtment.objects.filter(employtment_name__icontains=query)
    if jobs.exists():
        context['sucess']=True
    context['jobs']= jobs
    template_name = 'core/list_employtment.html'
    return render(request, template_name, context)


def detail_employtment(request, id):
    context = {}
    job = Employtment.objects.get(id=id)
    context['job']=job
    template_name = 'core/detail_employtment.html'
    return render(request,template_name, context)


@login_required
@company_required
def new_employtment(request):
    context = {}
    template_name = 'core/new_employtment.html'
    form = EmploytmentForm(request.POST or None)
    context['form'] = form
    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.company = request.user
            user.save()
            context['sucess'] = True
    return render(request, template_name, context)


@login_required
@candidate_required
def apply_for_employtment(request,id):
    user = Candidate.objects.get(user_id=request.user.id)
    employtment = get_object_or_404(Employtment, id=id) 
    apply_for, created = Apply_for.objects.get_or_create(candidate=user,job=employtment)
    return redirect('candidate_enrollment')


@login_required
@candidate_required
def cancel_enrollment(request,id):
    context = {}
    template_name = 'core/delete_confirmation.html'
    enrollment = Apply_for.objects.get(id=id)
    if request.method =="POST" and enrollment.candidate.user == request.user:
        enrollment.delete()
        return redirect('candidate_enrollment')
    else:
        context['obj'] = enrollment 
        return render(request, template_name, context)

