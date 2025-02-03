# payment_processing/views.py

import stripe
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import TemplateView

# Set your Stripe secret key
stripe.api_key = settings.STRIPE_SECRET_KEY


class  SuccessView(TemplateView):
    template_name = 'payment/success.html'

class CancelView(TemplateView):
    template_name ='payment/cancel.html'

def create_checkout_session(request):
    try:
        # Create a new Stripe Checkout session
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': 'Student Registration Fee',
                        },
                        'unit_amount': 5000,  # Amount in cents
                    },
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url=request.build_absolute_uri('/payment/success/'),
            cancel_url=request.build_absolute_uri('/payment/cancel/'),
        )

        return redirect(checkout_session.url, code=303)

    except Exception as e:
        return JsonResponse({'error': str(e)})

def payment_success(request):
    return render(request, 'payment/success.html')

def payment_cancel(request):
    return render(request, 'payment/cancel.html')
