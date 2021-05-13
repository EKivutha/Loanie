from . import views
from django.conf.urls import url

app_name = "main"

urlpatterns = [
    url(r'^$',views.homepage, name="homepage"),
    url(r'^loan_type/$', views.loan_types, name='loantype'),
    url(r'^client/$',views.apply_loan, name="applyloan"),
    
]