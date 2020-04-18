from django.urls import path

from .views import search,new_employtment,detail_employtment,apply_for_employtment,cancel_enrollment

urlpatterns = [
    path('pesquisa/',search, name='employtment_search'),
    path('nova-vaga/',new_employtment, name='employtment_new_employtment'),
    path('pesquisa/detalhes/<int:id>',detail_employtment, name='employtment_detail'),
    path('pesquisa/detalhes/inscricao/<int:id>',apply_for_employtment, name='employtment_apply_for'),
    path('pesquisa/inscricao/cancel/<int:id>',cancel_enrollment, name='candidate_cancel_enrollment'),
]
