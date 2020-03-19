from django.db import models
from localflavor.br.models import BRCNPJField

SITUATION = (
    ('1','Ativo'),
    ('2','Baixado'),
    ('3','Transferido')
)

class Customer(models.Model):
    code = models.CharField(max_length=10)           
    company = models.CharField(max_length=40)           
    name = models.CharField(max_length=100)             
    cnpj = BRCNPJField()             
    situation = models.CharField(max_length=1, choices=SITUATION)

class Contact(models.Model):
    name = models.CharField(max_length=100)          
    cel = models.CharField(max_length=14)         
    email = models.CharField(max_length=30)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  

class Adress(models.Model):
    street = models.CharField(max_length=100)
    number = models.CharField(max_length=7)          
    complement = models.CharField(max_length=100)      
    neighborhood = models.CharField(max_length=100)
    city = models.CharField(max_length=20)
    estate = models.CharField(max_length=15)
    zipcode = models.CharField(max_length=8)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  
