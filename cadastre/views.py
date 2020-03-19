import csv, io
from django.shortcuts import render,redirect, HttpResponse
from .forms import CustomerForm, CustomerAdressForm, ContactForm
from .models import Customer, Adress, Contact

def customer_list(request):
    qs = Customer.objects.all()
    code_contains_query = request.GET.get('code_contains')
    company_contains_query = request.GET.get('company_contains')
    situation_contains_query = request.GET.get('situation_contains')
    print(situation_contains_query,"BAAAAA")
    if situation_contains_query !='' and situation_contains_query is not None:
        qs = qs.filter(situation__icontains=situation_contains_query)
    if code_contains_query !='' and code_contains_query is not None:
        qs = qs.filter(code__icontains=code_contains_query)   
    if company_contains_query !='' and company_contains_query is not None:
        qs = qs.filter(company__icontains=company_contains_query)
    context = {'customer_list':qs}
    return render(request,"cadastre/customer_list.html",context)

def customer_form(request,id=0):
    if request.method == "GET":
        context = {'contact_list':Contact.objects.all()}
        if id==0:
            form = CustomerForm()
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(instance=customer)
        return render(request,"cadastre/customer_form.html", {'form':form,  'title': 'Cliente'})
    else:
        if id == 0:
            form = CustomerForm(request.POST)
        else:
            customer = Customer.objects.get(pk=id)
            form = CustomerForm(request.POST,instance=customer)
        if form.is_valid():
            form.save()
        else:
            form = CustomerForm()
            print('deu erro')
            return render(request,"cadastre/customer_form.html", {'form':form,  'title': 'Cliente', 'error': 'CNPJ INVALIDO'})
        return  redirect('/customer')

def customer_delete(request,id):
    print('chegou1')
    customer = Customer.objects.get(pk=id)
    customer.delete()
    return redirect('/customer/list')

def customer_adress_form(request,idCustomer=0, idAdress=0):
    if request.method == "GET":
        if idCustomer!=0:
            if idAdress==0:
                customer = Customer.objects.get(pk=idCustomer)
                form = CustomerAdressForm()
                form.fields["customer"].initial = customer
            else:
                adress = Adress.objects.get(pk=idAdress)
                form = CustomerAdressForm(instance=adress)
        return render(request,"cadastre/customer_form.html", {'form':form,  'title': 'Endereço'})
    else:
        if idAdress == 0:
            form = CustomerAdressForm(request.POST)
        else:
            adress = adress.objects.get(pk=idAdress)
            form = CustomerAdressForm(request.POST,instance=adress)
        if form.is_valid():
            form.save()
    context = {
        'customer_adress_list':Adress.objects.filter(customer__id=idCustomer),
        'idCustomer': idCustomer,
        'customer': Customer.objects.get(pk=idCustomer)
    }
    return render(request, "cadastre/customer_adress_list.html", context)


def customer_adress_list(request, idCustomer=0):
    context = {
        'customer_adress_list':Adress.objects.filter(customer__id=idCustomer),
        'idCustomer': idCustomer,
        'customer': Customer.objects.get(pk=idCustomer)
    }
    return render(request,"cadastre/customer_adress_list.html",context)  

def customer_adress_delete(request,idAdress):

    adress = Adress.objects.get(pk=idAdress)
    idCustomer = adress.customer.id
    adress.delete()
    context = {
        'customer_adress_list':Adress.objects.filter(customer__id=idCustomer),
        'idCustomer': idCustomer,
        'customer': Customer.objects.get(pk=idCustomer)
    }
    return render(request,"cadastre/customer_adress_list.html",context) 


def contact_list(request, idCustomer=0):
    context = {
        'contact_list':Contact.objects.filter(customer__id=idCustomer),
        'idCustomer': idCustomer,
        'customer': Customer.objects.get(pk=idCustomer)
    }
    return render(request,"cadastre/contact_list.html",context)        

def contact_form(request,idCustomer=0, idContact = 0):
    if request.method == "GET":      
        if idCustomer!=0: #se cliente =0 nao faz nada
            if idContact == 0:
                customer = Customer.objects.get(pk=idCustomer)
                form = ContactForm()
                form.fields["customer"].initial = customer
            else:
                contact = Contact.objects.get(pk=idContact)
                form = ContactForm(instance=contact)
        return render(request,"cadastre/customer_form.html", {'form':form, 'title': 'Contato'})
    else:
        if idContact == 0:
            form = ContactForm(request.POST)
        else:
            contact = Contact.objects.get(pk=idContact)
            form = ContactForm(request.POST,instance=contact)
        if form.is_valid():
            form.save()
    context = {
        'contact_list':Contact.objects.filter(customer__id=idCustomer),
        'idCustomer': idCustomer,
        'customer': Customer.objects.get(pk=idCustomer)
    }
    return render(request,"cadastre/contact_list.html",context)    


def contact_delete(request,idContact):

    contact = Contact.objects.get(pk=idContact)
    idCustomer = contact.customer.id
    contact.delete()
    context = {
        'contact_list':Contact.objects.filter(customer__id=idCustomer),
        'idCustomer': idCustomer,
        'customer': Customer.objects.get(pk=idCustomer)
    }
    return render(request,"cadastre/contact_list.html",context)  

def customer_download(request):
    customers = Customer.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename= "Cliente.csv"'

    writer = csv.writer(response, delimiter = ',')
    writer.writerow(['Codigo','Razao Social','CNPJ','Situacao'])
    for obj in customers:
        writer.writerow([obj.code, obj.company, obj.cnpj, obj.situation])

    return response


