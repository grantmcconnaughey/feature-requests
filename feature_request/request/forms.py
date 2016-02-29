from django import forms

from feature_request.request.models import FeatureRequest


class FeatureRequestForm(forms.ModelForm):

    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority',
                  'product_area', 'target_date', 'ticket_url']

    def save(self, commit=True):
        data = self.cleaned_data

        prior_client_priority_requests = FeatureRequest.objects.filter(
            client=data['client'], client_priority=data['client_priority'])

        # If this client already has feature requests at this priority
        if prior_client_priority_requests.exists():
            # Bump up each client priority by 1 to make room for the new request
            # Note: This doesn't scale well. Change the client priority to use
            # linked nodes so that inserts don't require updating every other
            # feature request for this client.
            for feature_request in prior_client_priority_requests:
                feature_request.client_priority += 1
                feature_request.save()

        return super(FeatureRequestForm, self).save(commit)
