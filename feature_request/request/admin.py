from django.contrib import admin

from .models import FeatureRequest, ProductArea, Client

admin.site.register(Client)
admin.site.register(ProductArea)
admin.site.register(FeatureRequest)
