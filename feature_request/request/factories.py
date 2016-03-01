from django.utils import timezone
import factory
from factory import DjangoModelFactory

from feature_request.request.models import Client, ProductArea, FeatureRequest


class ClientFactory(DjangoModelFactory):
    class Meta:
        model = Client
        django_get_or_create = ('name',)

    name = 'Test Client'


class ProductAreaFactory(DjangoModelFactory):
    class Meta:
        model = ProductArea
        django_get_or_create = ('name',)

    name = 'Billing'


class FeatureRequestFactory(DjangoModelFactory):
    class Meta:
        model = FeatureRequest

    title = 'Feature Request'
    description = 'Please do this thing!'
    client = factory.SubFactory(ClientFactory)
    client_priority = 1
    product_area = factory.SubFactory(ProductAreaFactory)
    target_date = timezone.now().date()
    ticket_url = 'http://google.com'
