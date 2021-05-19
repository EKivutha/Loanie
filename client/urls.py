from . import views
from django.conf.urls import url
from django.urls import path, include

app_name = "main"

urlpatterns = [
    url(r'^$',views.homepage, name="homepage"),
    url(r'^loan_type/$', views.loan_types, name='loantype'),
    url(r'^client/$',views.apply_loan, name="applyloan"),
    url(r'^settings/$',views.settings, name="settings"),
    path('daraja/stk-push/', views.stk_push_callback, name='mpesa_stk_push_callback'),
    
]