from django import forms
from .models import Customer
from .models import Adress
from .models import Contact
from django.forms import HiddenInput

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('code','company', 'name', 'cnpj', 'situation')
        labels = { 
            'code':'Código',
            'company':'Razão Social',
            'name':'Nome Fantasia',
            'cnpj':'CNPJ',
            'situation':'Situação'
        }

    def __init__(self, *args, **kwargs):
        super(CustomerForm, self). __init__(*args, **kwargs)

class CustomerAdressForm(forms.ModelForm): 

    class Meta:
        model = Adress
        fields = ('street','number', 'complement', 'neighborhood', 'city','estate','zipcode', 'customer')
        labels = { 
            'street':'Logradouro',
            'number':'Número',
            'complement':'Complemento',
            'neighborhood':'Bairro',
            'city':'Cidade',
            'Estate':'Estado',
            'zipcode':'CEP'
        }

    def __init__(self, *args, **kwargs):
        super(CustomerAdressForm, self). __init__(*args, **kwargs)  
        self.fields['customer'].widget = HiddenInput()

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('name','cel', 'email', 'customer')
        labels = { 
            'name':'Nome',
            'cel':'Telefone',
            'email':'Email'
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self). __init__(*args, **kwargs)  
        self.fields['customer'].widget = HiddenInput()

