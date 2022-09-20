import os

import stripe
from stripe.api_resources.price import Price
from stripe.api_resources.checkout.session import Session

# API_KEY = 'sk_test_51LjeHPGQS6hNySCITgx25ejHFML424Zjy3wczSayJ1VftGQqKJdM8CNDje7PHUWswvjTukt2FIPrSqJCYhOn9vnV00sQ49mF4m'
# PRODUCT = 'prod_MSZvRUKqY276GT'
# uri = request.escape_uri_path('success.html')


class StripeAPI:
    stripe.api_key = os.environ.get('STRIPE_API_KEY')
    product = os.environ.get('STRIPE_PRODUCT_KEY')

    def __init__(self, price: int, host: str):
        self.price = price
        self.host = host

    def _create_price(self) -> Price:
        return stripe.Price.create(
            unit_amount=self.price,
            currency="usd",
            product=self.product
        )

    def create_session(self) -> dict:
        stripe_session: Session = stripe.checkout.Session.create(
            success_url=f'http://{self.host}/static/success.html',
            cancel_url=f'http://{self.host}/static/cancel.html',
            line_items=[
                {
                    "price": self._create_price().id,
                    'quantity': 1,
                },
            ],
            mode='payment',
        )
        return {'stripe_session_id': stripe_session.id}


if __name__ == '__main__':
    stripe_api = StripeAPI(540)
    session = stripe_api.create_session()
    print(session)
    print(type(session))
