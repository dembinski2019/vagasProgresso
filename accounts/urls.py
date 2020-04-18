from django.urls import path,include
from .views import candidate, company
from .views.profile import (profile, edit_profile_candidate,edit_profile_company, 
                my_employtment, my_profile, 
                candidate_apply_for_amploytment,
                candidate_enrollment,candidate_enrollment_download_curriculum)


urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    
    path('profile/', profile, name='conta_profile'),
    path('profile/list/vagas/', my_employtment, name='list_my_employtment'),
    path('profile/list/vagas/inscritos/<int:id>', candidate_apply_for_amploytment, name='candidate_apply_for_amploytment'),   

    path('profile/edit/candidate/', edit_profile_candidate, name='conta_edit_profile_candidate'),
    path('profile/edit/company', edit_profile_company, name='conta_edit_profile_company'),
    path('profile/my/', my_profile, name='conta_my_profile'),
    
    path('profile/my/vagas/inscricoes/', candidate_enrollment, name='candidate_enrollment'),   
    path('profile/my/vagas/inscricoes/curriculo/', candidate_enrollment_download_curriculum, name='candidate_enrollment_download_curriculum'),   
    
    path('cadastro-candidato/', candidate.CandidateSignUpView.as_view(), name='cadastro_candidate'),
    path('cadastro-empresa/', company.CompanySignUpView.as_view(), name='cadastro_company'),
]
