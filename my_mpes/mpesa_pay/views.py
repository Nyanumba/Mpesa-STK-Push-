from django.shortcuts import render
from django.http import HttpResponse
from django_daraja.mpesa.core import MpesaClient

# Function views
def index(request):
    # Instantiate MpesaClient
    cl = MpesaClient()
    
    # Set transaction parameters
    phone_number = '254797469560'  # Ensure this number is in the format '2547XXXXXXX'
    amount = 1
    account_reference = 'reference'
    transaction_desc = 'Description'
    callback_url = 'https://darajambili.herokuapp.com/express-payment'  # Update if necessary

    # Call stk_push and handle the response
    response = cl.stk_push(
        phone_number=phone_number, 
        amount=amount, 
        account_reference=account_reference, 
        transaction_desc=transaction_desc, 
        callback_url=callback_url
    )
    return HttpResponse(f"STK Push Response: {response}")

def stk_push_callback(request):
    # Parse the incoming callback data (MPESA response)
    if request.method == 'POST':
        data = request.body
        # Add logic to handle the callback data, e.g., log it, save to DB, etc.
        print(data)  # Debugging
        return HttpResponse("STK Push Callback Received")
    return HttpResponse("Invalid Method", status=405)
