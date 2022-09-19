from decimal import Decimal
from stripe.api_resources.price import Price
from stripe.api_resources.checkout.session import Session

import stripe

API_KEY = 'sk_test_51LjeHPGQS6hNySCITgx25ejHFML424Zjy3wczSayJ1VftGQqKJdM8CNDje7PHUWswvjTukt2FIPrSqJCYhOn9vnV00sQ49mF4m'
PRODUCT = 'prod_MSZvRUKqY276GT'


class StripeAPI:
    stripe.api_key = API_KEY
    product = PRODUCT

    def __init__(self, price: int):
        self.price = price

    def _create_price(self) -> Price:
        return stripe.Price.create(
            unit_amount=self.price,
            currency="usd",
            product=self.product
        )

    def create_session(self) -> dict:
        stripe_session: Session = stripe.checkout.Session.create(
            success_url='https://example.com/success',
            cancel_url='https://example.com/cancel',
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
    stripe_api = StripeAPI(price=Decimal('450.30'))
    session = stripe_api.create_session()
    print(session)
    print(type(session))
