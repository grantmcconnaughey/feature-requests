from django import forms

from feature_request.request.models import FeatureRequest


class FeatureRequestForm(forms.ModelForm):

    class Meta:
        model = FeatureRequest
        fields = ['title', 'description', 'client', 'client_priority',
                  'product_area', 'target_date', 'ticket_url']
        widgets = {
            'target_date': forms.TextInput(attrs={'placeholder': 'MM/DD/YYYY'}),
        }

    def save(self, commit=True):
        if commit:
            # All other instance fields are set elsewhere. Make sure
            # client_priority is set to None initially so that it will be
            # updated when we call self.instance.to()
            self.instance.client_priority = None
            self.instance.save()

            # Set this feature request's client_priority field and moves all
            # other feature requests (if necessary)
            self.instance.to(self.cleaned_data['client_priority'])

        return self.instance
