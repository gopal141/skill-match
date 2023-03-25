from django.urls import path
from . import views

urlpatterns = [
    path('error', views.error, name="errorpage"),
    path('about', views.about, name="aboutpage"),
    path('candidatesingle', views.candidatesingle, name="candidatesinglepage"),
    path('candidateslist', views.candidateslist,name="candidateslistpage"),
    path('candidatessingle', views.candidatessingle,name="candidatessinglepage"),
    path('contact', views.contact,name="contactpage"),
    path('employerlist', views.employerlist,name="employerlistpage"),
    path('employersingle',views.employersingle,name="employersinglepage"),
    path('how',views.how,name="howpage"),
    path('', views.index,name="homepage"),
    path('locationsingle',views.locationsingle,name="locationpage"),
    path('pricing',views.pricing,name="pricingpage"),
    path('services',views.services,name="servicespage")
]
