from django.db import models
from django.conf import settings
from accounts.models import Candidate


class Employtment(models.Model):
    employtment_name = models.CharField('Nome da Vaga', max_length=150) 
    slug = models.SlugField('Palavra chave')
    requirements = models.TextField('Requisitos') 
    description = models.TextField('Descrição') 
    salary = models.DecimalField('Salário', max_digits=8, decimal_places=2)
    jobs_vacancy = models.IntegerField("Quantidade de Vagas")
    company = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name="Empresa", on_delete=models.CASCADE) 
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)
    
    
    def get_absolute_url(self):
        from django.shortcuts import reverse
        return reverse('employtment_detail', kwargs={'slug': self.slug})

    def __str__(self):
        return self.employtment_name
        
    class Meta:
        verbose_name = 'Vaga'
        verbose_name_plural = 'Vagas'
        ordering =['employtment_name']




class Apply_for(models.Model):
    job = models.ForeignKey(Employtment, verbose_name=("Vaga"),related_name='apply_for', on_delete=models.CASCADE)
    candidate = models.ForeignKey(Candidate, verbose_name=("Candidato"),related_name='apply_for', on_delete=models.CASCADE)
    created_at = models.DateTimeField(verbose_name="Criado em", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Atualizado em", auto_now=True)
   
    def __str__(self):
        return f'{self.job.company} - {self.job.employtment_name} - {self.candidate.user.username}'

    
    class Meta:
        verbose_name="Inscrição"
        verbose_name_plural="Inscrições"
        unique_together = [['candidate', 'job']]
    
