

from django.urls import path, re_path
from . import views
app_name ='app'
urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('transaction/', views.transactions, name='transaction'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
