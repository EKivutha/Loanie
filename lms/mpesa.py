from django_daraja.mpesa.core import MpesaClient

phone_number = '07xxxxxxxx'
amount = 1
transaction_desc = 'Description'
occassion = 'Occassion'
callback_url = request.build_absolute_uri(reverse('mpesa_salary_payment_callback'))
response = self.cl.business_payment(phone_number, amount, transaction_desc, self.callback_url, occassion)


def index(request):
    cl = MpesaClient()
    phone_number = '0700111222'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = request.build_absolute_uri(reverse('mpesa_stk_push_callback'))
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    return HttpResponse(response)