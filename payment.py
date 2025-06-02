import stripe
from config import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY

def create_payment(amount, currency='usd'):
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        payment_method_types=['card'],
    )
    return intent.client_secret
