import datetime
from django.core.urlresolvers import reverse
from django.test import TestCase

from feature_request.request.factories import FeatureRequestFactory, \
    ClientFactory, ProductAreaFactory
from feature_request.request.forms import FeatureRequestForm
from feature_request.request.models import FeatureRequest


class FeatureRequestTests(TestCase):

    def test_list(self):
        feature_request = FeatureRequestFactory()
        url = reverse('index')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(list(response.context['feature_requests']),
                         [feature_request])

    def test_detail(self):
        feature_request = FeatureRequestFactory()
        url = reverse('detail', args=[feature_request.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['feature_request'], feature_request)

    def test_create_get(self):
        url = reverse('create')

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], FeatureRequestForm)

    def test_create_post_creates_new_feature_request(self):
        client = ClientFactory()
        product_area = ProductAreaFactory()
        url = reverse('create')

        response = self.client.post(url, data={
            'title': 'New Request',
            'description': 'Do something',
            'client': client.pk,
            'client_priority': 1,
            'product_area': product_area.pk,
            'target_date': '01/01/2016',
            'ticket_url': 'http://google.com',
        })

        feature_request = FeatureRequest.objects.get()
        self.assertEqual(feature_request.title, 'New Request')
        self.assertEqual(feature_request.description, 'Do something')
        self.assertEqual(feature_request.client, client)
        self.assertEqual(feature_request.client_priority, 1)
        self.assertEqual(feature_request.product_area, product_area)
        self.assertEqual(feature_request.target_date, datetime.date(2016, 1, 1))
        self.assertEqual(feature_request.ticket_url, 'http://google.com')

    def test_create_post_bumps_the_client_priority_number(self):
        client = ClientFactory()
        product_area = ProductAreaFactory()
        feature_request = FeatureRequestFactory(client=client,
                                                client_priority=1)
        url = reverse('create')

        response = self.client.post(url, data={
            'title': 'New Request',
            'description': 'Do something',
            'client': client.pk,
            'client_priority': 1,
            'product_area': product_area.pk,
        })

        # The new request now gets client priority 1
        new_request = FeatureRequest.objects.exclude(pk=feature_request.pk).get()
        self.assertEqual(new_request.client, client)
        self.assertEqual(new_request.client_priority, 1)

        # The old request gets its priority bumps to 2
        original_request = FeatureRequest.objects.get(pk=feature_request.pk)
        self.assertEqual(original_request.client, client)
        self.assertEqual(original_request.client_priority, 2)

    def test_create_post_redirects_to_list(self):
        client = ClientFactory()
        product_area = ProductAreaFactory()
        url = reverse('create')

        response = self.client.post(url, data={
            'title': 'New Request',
            'description': 'Do something',
            'client': client.pk,
            'client_priority': 1,
            'product_area': product_area.pk,
            'target_date': '01/01/2016',
            'ticket_url': 'http://google.com',
        })

        expected_url = reverse('index')
        self.assertRedirects(response, expected_url)

    def test_update_get(self):
        feature_request = FeatureRequestFactory()
        url = reverse('update', args=[feature_request.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.context['form'], FeatureRequestForm)
        self.assertEqual(response.context['feature_request'], feature_request)

    def test_update_post_updates_new_feature_request(self):
        client = ClientFactory()
        product_area = ProductAreaFactory()
        feature_request = FeatureRequestFactory()
        url = reverse('update', args=[feature_request.pk])

        response = self.client.post(url, data={
            'title': 'Updated Request',
            'description': 'Do something else',
            'client': client.pk,
            'client_priority': 2,
            'product_area': product_area.pk,
            'target_date': '02/01/2016',
            'ticket_url': 'http://facebook.com',
        })

        feature_request = FeatureRequest.objects.get()
        self.assertEqual(feature_request.title, 'Updated Request')
        self.assertEqual(feature_request.description, 'Do something else')
        self.assertEqual(feature_request.client, client)
        self.assertEqual(feature_request.client_priority, 2)
        self.assertEqual(feature_request.product_area, product_area)
        self.assertEqual(feature_request.target_date, datetime.date(2016, 2, 1))
        self.assertEqual(feature_request.ticket_url, 'http://facebook.com')

    def test_update_post_redirects_to_list(self):
        client = ClientFactory()
        product_area = ProductAreaFactory()
        feature_request = FeatureRequestFactory()
        url = reverse('update', args=[feature_request.pk])

        response = self.client.post(url, data={
            'title': 'Updated Request',
            'description': 'Do something else',
            'client': client.pk,
            'client_priority': 2,
            'product_area': product_area.pk,
            'target_date': '02/01/2016',
            'ticket_url': 'http://facebook.com',
        })

        expected_url = reverse('index')
        self.assertRedirects(response, expected_url)

    def test_delete_get(self):
        feature_request = FeatureRequestFactory()
        url = reverse('delete', args=[feature_request.pk])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['feature_request'], feature_request)

    def test_delete_post_deletes_feature_request(self):
        feature_request = FeatureRequestFactory()
        url = reverse('delete', args=[feature_request.pk])

        response = self.client.post(url)

        self.assertEqual(FeatureRequest.objects.count(), 0)

    def test_delete_post_deletes_redirects_to_list(self):
        feature_request = FeatureRequestFactory()
        url = reverse('delete', args=[feature_request.pk])

        response = self.client.post(url)

        expected_url = reverse('index')
        self.assertRedirects(response, expected_url)


class FeatureRequestModelTests(TestCase):

    def test_feature_request_str_returns_title(self):
        feature_request = FeatureRequestFactory(title='New Request')

        self.assertEqual(str(feature_request), 'New Request')
