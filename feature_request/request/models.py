from django.core.urlresolvers import reverse
from django.db import models
from django.utils.six import python_2_unicode_compatible
from ordered_model.models import OrderedModelBase


@python_2_unicode_compatible
class Client(models.Model):

    name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class ProductArea(models.Model):

    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class FeatureRequest(OrderedModelBase):

    title = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(Client)
    client_priority = models.PositiveIntegerField(db_index=True, null=True,
                                                  blank=True)
    product_area = models.ForeignKey(ProductArea)
    target_date = models.DateField(null=True, blank=True)
    ticket_url = models.URLField(null=True, blank=True)
    order_field_name = 'client_priority'

    class Meta:
        ordering = ('client', 'client_priority')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', args=[self.pk])
