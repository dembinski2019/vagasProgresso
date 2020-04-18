from django.db import models

from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_candidate = models.BooleanField(verbose_name='Candidato', default=False)
    is_company = models.BooleanField(verbose_name='Empresa',default=False)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering = ['username']

class Candidate(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    cpf = models.CharField('CPF', max_length=11)
    whatsapp = models.CharField('WhatsApp', max_length=12)
    curriculum = models.FileField("Curriculo", upload_to=f'static/candidate/curriculum', max_length=100)
    
    def __str__(self):
        return self.user.username
        
    def chage_view(self):
        return self.curriculum

class Company(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,primary_key=True)
    cnpj = models.CharField('CNPJ', max_length=11)
    whatsapp = models.CharField('WhatsApp', max_length=12)
    responsibly = models.CharField('Responsável', max_length=150)
    
    def __str__(self):
        return self.user.username
    
