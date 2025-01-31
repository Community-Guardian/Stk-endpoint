from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_daraja.mpesa.core import MpesaClient
from decouple import config

@api_view(['POST'])
def make_stk_push(request):
    amount = request.data.get('amount')
    phone_number = request.data.get('phone_number')

    if amount is None or phone_number is None:
        return Response({'error': 'Amount and phone number are required.'}, status=status.HTTP_400_BAD_REQUEST)

    try:
        amount = int(amount)
    except ValueError:
        return Response({'error': 'Amount must be a number.'}, status=status.HTTP_400_BAD_REQUEST)

    account_reference = 'ABC001'
    transaction_desc = 'STK Push Description'
    callback_url = config('STK_PUSH_CALLBACK_URL')

    cl = MpesaClient()
    response = cl.stk_push(phone_number, amount, account_reference, transaction_desc, callback_url)
    
    return Response({'response_description': response.response_description})