from django.shortcuts import render

def index(request):
    template_view = 'website/index.html'
    return render(request, template_view)

def company(request):
    template_view = 'website/company_home.html'
    return render(request, template_view)

def candidate(request):
    template_view = 'website/candidate_home.html'
    return render(request, template_view)

