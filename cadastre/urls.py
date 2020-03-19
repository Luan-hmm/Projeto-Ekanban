from django.urls import path,include
from . import views 

urlpatterns = [
    path('', views.customer_form, name='customer_insert'),
    path('<int:id>/', views.customer_form, name='customer_update'),
    path('list/', views.customer_list, name='customer_list'),
    path('delete/<int:id>/', views.customer_delete, name='customer_delete'),

    path('adress/<int:idCustomer>/', views.customer_adress_form, name='adress_insert'),
    path('adress/list/<int:idCustomer>', views.customer_adress_list, name='adress_list'), 
    path('adress/<int:idAdress>/<int:idCustomer>', views.customer_adress_form, name='adress_update'),
    path('adress/delete/<int:idAdress>/', views.customer_adress_delete, name='adress_delete'), 

    path('contact/<int:idCustomer>/', views.contact_form, name='contact_insert'),
    path('contact/list/<int:idCustomer>', views.contact_list, name='contact_list'),    
    path('contact/<int:idContact>/<int:idCustomer>', views.contact_form, name='contact_update'),
    path('contact/delete/<int:idContact>/', views.contact_delete, name='contact_delete'),

    path('download',views.customer_download, name='customer_download'),

]