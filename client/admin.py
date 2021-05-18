from django.contrib import admin

# Register your models here.
from .models import Loan,LoanTypes,Payments

admin.site.register(LoanTypes)
admin.site.register(Loan)
admin.site.register(Payments)